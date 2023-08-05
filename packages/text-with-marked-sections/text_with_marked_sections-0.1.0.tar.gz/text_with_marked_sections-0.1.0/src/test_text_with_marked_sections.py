import pytest
# from .. import TextWithMarkedSections

# from "text-with-marked-sections" import TextWithMarkedSections
from text_with_marked_sections import TextWithMarkedSections
from text_with_marked_sections import MissingEndMarker, MissingStartMarker, EndMarkerBeforeStartMarker, MultipleStartMarkers, MultipleEndMarkers


class TestClassFlantContent:
    def test_no_flant_content(self):
        content = "line 1\n line 2"
        configProcessor = TextWithMarkedSections(content)
        configProcessor.parse()

        expected = ''
        actual = configProcessor.get_marked_content()
        assert actual == expected

    def test_flant_content_single_line(self):
        content = """pre line 1
### START ###
flant line 1
### END ###
post line 1
"""
        configProcessor = TextWithMarkedSections(content)
        configProcessor.parse()

        expected = 'flant line 1'
        actual = configProcessor.get_marked_content()
        assert actual == expected

    def test_flant_content_multiline(self):
        content = """pre line 1
### START ###
flant line 1
flant line 2
### END ###
post line 1
"""
        configProcessor = TextWithMarkedSections(content)
        configProcessor.parse()

        expected = 'flant line 1\nflant line 2'
        actual = configProcessor.get_marked_content()
        assert actual == expected


class TestClassPreContent:
    def test_pre_multiline(self):
        content = "line 1\nline 2"
        configProcessor = TextWithMarkedSections(content)
        configProcessor.parse()

        expected = "line 1\nline 2"
        actual = configProcessor.get_user_content_pre()
        assert actual == expected

    def test_pre_single_line(self):
        content = "line"
        configProcessor = TextWithMarkedSections(content)
        configProcessor.parse()

        expected = "line"
        actual = configProcessor.get_user_content_pre()
        assert actual == expected

    def test_pre_empty(self):
        content = ""
        configProcessor = TextWithMarkedSections(content)
        configProcessor.parse()

        expected = ""
        actual = configProcessor.get_user_content_pre()
        assert actual == expected


class TestClassRender:

    def test_render_empty(self):
        content = ""
        new_content = "new line"
        expected = """### START ###
new line
### END ###"""
        configProcessor = TextWithMarkedSections(content)
        configProcessor.parse()
        actual = configProcessor.render_with_data(new_content)
        assert actual == expected

    def test_render_one_line(self):
        content = "original line"
        new_content = "new line"
        expected = """original line
### START ###
new line
### END ###"""
        configProcessor = TextWithMarkedSections(content)
        configProcessor.parse()
        actual = configProcessor.render_with_data(new_content)
        assert actual == expected

    def test_render_update1(self):
        content = """line 1
### START ###
old line
### END ###
line 2
"""
        new_content = "new line"
        expected = """line 1
### START ###
new line
### END ###
line 2
"""
        configProcessor = TextWithMarkedSections(content)
        configProcessor.parse()
        actual = configProcessor.render_with_data(new_content)
        assert actual == expected

    def test_render_update2(self):
        content = """### START ###
old line
### END ###
user line
"""
        new_content = "new line"
        expected = """### START ###
new line
### END ###
user line
"""
        configProcessor = TextWithMarkedSections(content)
        configProcessor.parse()
        actual = configProcessor.render_with_data(new_content)
        assert actual == expected


class TestClassExceptions:

    def test_Exception_MissingEndMarker(self):
        content = """
### START ###
"""
        configProcessor = TextWithMarkedSections(content)
        with pytest.raises(MissingEndMarker):
            configProcessor.parse()

    def test_Exception_MultipleStartMarkers(self):
        content = """
### START ###
### START ###
### END ###
"""
        configProcessor = TextWithMarkedSections(content)
        with pytest.raises(MultipleStartMarkers):
            configProcessor.parse()

    def test_Exception_MultipleEndMarkers(self):
        content = """
### START ###
### END ###
### END ###
"""
        configProcessor = TextWithMarkedSections(content)
        with pytest.raises(MultipleEndMarkers):
            configProcessor.parse()

    def test_Exception_EndMarkerBeforeStartMarker(self):
        content = """
### END ###
### START ###
"""
        configProcessor = TextWithMarkedSections(content)
        with pytest.raises(EndMarkerBeforeStartMarker):
            configProcessor.parse()
