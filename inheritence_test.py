#!usr/bin/env python

_DOCUMENTATION = None
_EXAMPLES = None
HAS_LIB = False

try:
    from inheritence.child_verb_foo import DOCUMENTATION, EXAMPLES, main
    _DOCUMENTATION = DOCUMENTATION
    _EXAMPLES = EXAMPLES
    HAS_LIB = True
except Exception as e:
    msg = "Failed to generate!\nError{0}".format(e)
    raise ValueError(msg)

if __name__ == "__main__":
    print "Test started"
    print HAS_LIB

