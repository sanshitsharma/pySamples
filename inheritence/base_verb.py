#!/usr/bin/env python

class BaseVerb(object):
    #def __init__(self):
    def __init__(self, spec_file, HAS_LIB):
        print "initialized base class verb"
        self.__name = 'BaseVerb'

        if not HAS_LIB:
            msg = "error occured while loading libs"
            raise ValueError(msg)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self):
        raise Warning("cannot set name after init")