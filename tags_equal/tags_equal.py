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
        if closed:
            self.tag = self.tag[1:-1]     # strip open and closing brackets
        else:
            raise InvalidHTMLTagException("Unclosed tag.")

        has_tagname = len(self.tag) >= 1
        if has_tagname:
            self.tagname = self.tag.split(' ', 1)[0]
        else:
            raise InvalidHTMLTagException("Missing tagname.")

        # parse attributes
        try:
            attrs = self.tag.split(' ')[1:]
        except IndexError:
            return  # no attributes

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
        self.tag = tag.lower()
        self.tagname = ""
        self.attrs = {}

        # valid html tag?
        closed = self.tag.startswith('<') and self.tag.endswith('>')
        if closed:
            self.tag = self.tag[1:-1]     # strip open and closing brackets
        else:
            raise InvalidHTMLTagException("Unclosed tag.")

        has_tagname = len(self.tag) >= 1
        if has_tagname:
            self.tagname = self.tag.split(' ', 1)[0]
        else:
            raise InvalidHTMLTagException("Missing tagname.")

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
        self.tag = tag.lower()
        self.tagname = ""
        self.attrs = {}

        # valid html tag?
        closed = self.tag.startswith('<') and self.tag.endswith('>')
        if closed:
            self.tag = self.tag[1:-1]     # strip open and closing brackets
        else:
            raise InvalidHTMLTagException("Unclosed tag.")

        has_tagname = len(self.tag) >= 1
        if has_tagname:
            self.tagname = self.tag.split(' ', 1)[0]
        else:
            raise InvalidHTMLTagException("Missing tagname.")

        # parse attributes
        try:
            attrs = self.tag.split(' ')[1:]
        except IndexError:
            return  # no attributes

        for attr in attrs:  # no spaces in attr names
            try:
                key, val = attr.split('=')
            except ValueError:
                key, val = attr, None   # attribute w/o value

            if key not in self.attrs:   # only record first instance
                self.attrs[key] = val


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
        self.tag = tag.lower()
        self.tagname = ""
        self.attrs = {}

        # valid html tag?
        closed = self.tag.startswith('<') and self.tag.endswith('>')
        if closed:
            self.tag = self.tag[1:-1]     # strip open and closing brackets
        else:
            raise InvalidHTMLTagException("Unclosed tag.")

        has_tagname = len(self.tag) >= 1
        if has_tagname:
            self.tagname = self.tag.split(' ', 1)[0]
        else:
            raise InvalidHTMLTagException("Missing tagname.")

        # parse attributes
        try:
            attrs = self.tag.split(' ', 1)[1]
            import shlex
            attrs = shlex.split(attrs)  # quote aware splitting
        except IndexError:
            return  # no attributes


        for attr in attrs:  # no spaces in attr names
            try:
                key, val = attr.split('=')
            except ValueError:
                key, val = attr, None   # attribute w/o value

            val = val.replace("'", "").replace('"', '') # ignore quotes
            if key not in self.attrs:   # only record first instance
                self.attrs[key] = val


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
