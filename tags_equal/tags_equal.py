# Base
class InvalidHTMLTagException(Exception):
    pass

class HTMLTag:
    def __init__(self, tag):
        self.tag = tag.lower()
        self.tagname = ""
        self.attrs = {}

        # valid html tag?
        closed = self.tag.startswith('<') and self.tag.endswith('>')
        has_tagname = len(self.tag) >= 3
        if closed and has_tagname:
            self.tag = self.tag[1:-1]     # strip open and closing brackets
            self.tagname = self.tag.split(' ', 1)[0]
        else:
            raise InvalidHTMLTagException

        # parse attributes
        try:
            attrs = self.tag.split(' ')[1:]
        except IndexError:
            return  # no attributes

        for attr in attrs:  # no spaces in attr names
            key, val = attr.split('=')
            self.attrs[key] = val


    def __eq__(self, other):
        if self.tagname != other.tagname:
            return False
        return self.attrs == other.attrs


def tags_equal(tag1: str, tag2: str) -> bool:
    """Returns True if 2 HTML tags have the same attributes and values.

    >>> tags_equal("<img src=cats.jpg height=40>", "<IMG SRC=Cats.JPG height=40>")
    True
    >>> tags_equal("<img src=dogs.jpg width=99>", "<img src=dogs.jpg width=20>")
    False
    >>> tags_equal("<p>", "<P>")
    True
    >>> tags_equal("<b>", "<p>")
    False
    """
    return HTMLTag(tag1) == HTMLTag(tag2)


# Bonus 1
class InvalidHTMLTagException(Exception):
    pass

class HTMLTag:
    def __init__(self, tag):
        self.tag = tag.lower()
        self.tagname = ""
        self.attrs = {}

        # valid html tag?
        closed = self.tag.startswith('<') and self.tag.endswith('>')
        has_tagname = len(self.tag) >= 3
        if closed and has_tagname:
            self.tag = self.tag[1:-1]     # strip open and closing brackets
            self.tagname = self.tag.split(' ', 1)[0]
        else:
            raise InvalidHTMLTagException

        # parse attributes
        try:
            attrs = self.tag.split(' ')[1:]
        except IndexError:
            return  # no attributes

        for attr in attrs:  # no spaces in attr names
            key, val = attr.split('=')
            if key not in self.attrs:   # only record first instance
                self.attrs[key] = val


    def __eq__(self, other):
        if self.tagname != other.tagname:
            return False
        return self.attrs == other.attrs


def tags_equal(tag1: str, tag2: str) -> bool:
    """Returns True if 2 HTML tags have the same attributes and values.
    Ignores duplicate attributes.

    >>> tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_email>")
    True
    >>> tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_username>")
    False
    """
    return HTMLTag(tag1) == HTMLTag(tag2)
