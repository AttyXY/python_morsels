# Base
class InvalidHTMLTagException(Exception):
    pass

class HTMLTag:
    def __init__(self, tag):
        tag = tag.lower()

        # valid html tag?
        closed = tag.startswith('<') and tag.endswith('>')
        if closed:
            tag = tag[1:-1]     # strip open and closing brackets
        else:
            raise InvalidHTMLTagException("Unclosed tag.")

        # parse tagname
        has_tagname = len(tag) >= 1
        if has_tagname:
            self.tagname, *attrs = tag.split()
        else:
            raise InvalidHTMLTagException("Missing tagname.")

        # parse attributes
        self.attrs = {}
        for attr in attrs:  # no spaces in attr names
            key, val = attr.split('=')
            self.attrs[key] = val


    def __eq__(self, other):
        return (self.tagname == other.tagname and self.attrs == other.attrs)


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
    >>> tags_equal("<b>", "")
    Traceback (most recent call last):
    ...
    tags_equal.InvalidHTMLTagException: Unclosed tag.
    >>> tags_equal("<b>", "<>")
    Traceback (most recent call last):
    ...
    tags_equal.InvalidHTMLTagException: Missing tagname.
    """
    return HTMLTag(tag1) == HTMLTag(tag2)


# Bonus 1
class InvalidHTMLTagException(Exception):
    pass

class HTMLTag:
    def __init__(self, tag):
        tag = tag.lower()

        # valid html tag?
        closed = tag.startswith('<') and tag.endswith('>')
        if closed:
            tag = tag[1:-1]     # strip open and closing brackets
        else:
            raise InvalidHTMLTagException("Unclosed tag.")

        # parse tagname
        has_tagname = len(tag) >= 1
        if has_tagname:
            self.tagname, *attrs = tag.split()
        else:
            raise InvalidHTMLTagException("Missing tagname.")

        # parse attributes
        self.attrs = {}
        for attr in attrs:  # no spaces in attr names
            key, val = attr.split('=')
            self.attrs.setdefault(key, val)     # only record first instance


    def __eq__(self, other):
        return (self.tagname == other.tagname and self.attrs == other.attrs)


def tags_equal(tag1: str, tag2: str) -> bool:
    """Returns True if 2 HTML tags have the same attributes and values.
    Ignores duplicate attributes.

    >>> tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_email>")
    True
    >>> tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_username>")
    False
    """
    return HTMLTag(tag1) == HTMLTag(tag2)


# Bonus 2
class InvalidHTMLTagException(Exception):
    pass


class HTMLTag:
    def __init__(self, tag):
        tag = tag.lower()

        # valid html tag?
        closed = tag.startswith('<') and tag.endswith('>')
        if closed:
            tag = tag[1:-1]     # strip open and closing brackets
        else:
            raise InvalidHTMLTagException("Unclosed tag.")

        # parse tagname
        has_tagname = len(tag) >= 1
        if has_tagname:
            self.tagname, *attrs = tag.split()
        else:
            raise InvalidHTMLTagException("Missing tagname.")

        # parse attributes
        self.attrs = {}
        for attr in attrs:  # no spaces in attr names
            try:
                key, val = attr.split('=')
            except ValueError:
                key, val = attr, None   # attribute w/o value
            self.attrs.setdefault(key, val)     # only record first instance


    def __eq__(self, other):
        return (self.tagname == other.tagname and self.attrs == other.attrs)


def tags_equal(tag1: str, tag2: str) -> bool:
    """Returns True if 2 HTML tags have the same attributes and values.
    Ignores duplicate attributes. Allows attributes without values.

    >>> tags_equal("<OPTION NAME=Hawaii SELECTED>", "<option selected name=hawaii>")
    True
    >>> tags_equal("<option name=hawaii>", "<option name=hawaii selected>")
    False
    """
    return HTMLTag(tag1) == HTMLTag(tag2)


# Bonus 3
class InvalidHTMLTagException(Exception):
    pass

class HTMLTag:
    def __init__(self, tag):
        tag = tag.lower()

        # valid html tag?
        closed = tag.startswith('<') and tag.endswith('>')
        if closed:
            tag = tag[1:-1]     # strip open and closing brackets
        else:
            raise InvalidHTMLTagException("Unclosed tag.")

        # parse tagname
        has_tagname = len(tag) >= 1
        if has_tagname:
            import shlex
            self.tagname, *attrs = shlex.split(tag)  # quote aware splitting
        else:
            raise InvalidHTMLTagException("Missing tagname.")

        # parse attributes
        self.attrs = {}
        for attr in attrs:  # no spaces in attr names
            try:
                key, val = attr.split('=')
                val = val.replace("'", "").replace('"', '') # ignore quotes
            except ValueError:
                key, val = attr, None   # attribute w/o value

            self.attrs.setdefault(key, val)     # only record first instance


    def __eq__(self, other):
        return (self.tagname == other.tagname and self.attrs == other.attrs)


def tags_equal(tag1: str, tag2: str) -> bool:
    """Returns True if 2 HTML tags have the same attributes and values.
    Ignores duplicate attributes. Allows attributes without values.
    Handles single/double quoted attribute values.

    >>> tags_equal("<input value='hello there'>", '<input value="hello there">')
    True
    >>> tags_equal("<input value=hello>", "<input value='hello'>")
    True
    >>> tags_equal("<input value='hi friend'>", "<input value='hi there'>")
    False
    """
    return HTMLTag(tag1) == HTMLTag(tag2)
