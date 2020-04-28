# Base
class InvalidHTMLTagException(Exception):
    pass

class HTMLTag:
    def __init__(self, tag):
        self.og_tag = tag
        self.tagname = ""
        self.attrs = {}

        # valid html tag?
        closed = tag.startswith('<') and tag.endswith('>')
        has_tagname = len(tag) >= 3
        if closed and has_tagname:
            tag = tag[1:-1]     # strip open and closing brackets
            self.tagname = tag.split(' ', 1)[0].lower()    # get tagname
        else:
            raise InvalidHTMLTagException

        # parse attributes
        try:
            tag = tag.split(' ', 1)[1]
            attrs = tag.split('=')
        except IndexError:
            return  # no attributes

        key = attrs[0]
        for i in range(1, len(attrs)):
            temp = attrs[i].split(' ')
            val = temp[0]
            self.attrs[key.lower()] = val.lower()
            try:
                key = ' '.join(temp[1:])
            except IndexError:
                pass    # reached last key


    def __eq__(self, other):
        if self.tagname != other.tagname:
            return False

        for k,v in self.attrs.items():
            try:
                if other.attrs[k] != v:
                    return False    # value not the same
            except KeyError:
                return False    # does not contain key
        return True


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
