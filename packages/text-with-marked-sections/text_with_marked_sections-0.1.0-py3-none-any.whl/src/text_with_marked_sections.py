

class MultipleStartMarkers(Exception):
    pass


class MultipleEndMarkers(Exception):
    pass


class MissingStartMarker(Exception):
    pass


class MissingEndMarker(Exception):
    pass


class EndMarkerBeforeStartMarker(Exception):
    pass


class MultipleMarkers(Exception):
    pass


class MarkerNotFound(Exception):
    pass


    # USER_CONTENT_PRE = auto()
    # START_MARKER = auto()
    # MARKED_CONTENT = auto()
    # STOP_MARKER = auto()
    # USER_CONTENT_POST = auto()


class SectionClassifier:

    def __init__(self, start_marker: str, stop_marker: str) -> None:
        self.start_marker = start_marker
        self.stop_marker = stop_marker
        self.current_class = 'user_content_pre'

    def update_class(self, new_class: str):
        if self.current_class != new_class:
            self.current_class = new_class

    def get_class(self, line) -> str:
        """
        Returns a class of `line`. One of:
        - user_content_pre
        - start_marker
        - marked_content
        - stop_marker
        - user_content_post
        """
        if self.current_class == 'user_content_pre':
            if line == self.start_marker:
                self.update_class('marked_content')
                return 'start_marker'
            elif line == self.stop_marker:
                raise EndMarkerBeforeStartMarker
        elif self.current_class == 'marked_content':
            if line == self.start_marker:
                raise MultipleStartMarkers
            elif line == self.stop_marker:
                self.update_class('user_content_post')
                return 'stop_marker'
        elif self.current_class == 'user_content_post':
            if line == self.start_marker:
                raise MultipleStartMarkers
            elif line == self.stop_marker:
                raise MultipleEndMarkers
        return self.current_class

    def final_check(self) -> bool:
        """
        Returns `True` current state is OK to be a final state.

        Raises `MissingEndMarker` in case of error.
        """
        if self.current_class == 'marked_content':
            raise MissingEndMarker
        return True


class TextWithMarkedSections():
    def __init__(self, content: str, start_marker="### START ###", end_marker='### END ###') -> None:
        self.content = content
        self.start_marker = start_marker
        self.end_marker = end_marker

        self.sections = {
            'user_content_pre': [],
            'marked_content': [],
            'user_content_post': []
        }

    def parse(self):
        classifier = SectionClassifier(self.start_marker, self.end_marker)
        for line in self.content.split('\n'):
            line_class = classifier.get_class(line)
            if line_class != 'start_marker' and line_class != 'stop_marker':
                self.sections[classifier.current_class].append(line)

        classifier.final_check()

    def get_user_content_pre(self):
        if len(self.sections['user_content_pre']) > 0:
            content = '\n'.join(self.sections['user_content_pre'])
        else:
            content = ''
        return content

    def get_user_content_post(self):
        if len(self.sections['user_content_post']) > 0:
            content = '\n'.join(self.sections['user_content_post'])
        else:
            content = ''
        return content

    def get_marked_content(self):
        if len(self.sections['marked_content']) > 0:
            content = '\n'.join(self.sections['marked_content'])
        else:
            content = ''
        return content

    def render_with_data(self, new_content):
        pre_content = self.get_user_content_pre()
        post_content = self.get_user_content_post()

        parts = []
        if len(pre_content) > 0:
            parts.append(pre_content)
        parts.append(self.start_marker)
        parts.append(new_content)
        parts.append(self.end_marker)
        if len(post_content) > 0:
            parts.append(post_content)

        rendered_content = '\n'.join(parts)
        return rendered_content
