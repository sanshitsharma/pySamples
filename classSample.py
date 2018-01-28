#!/usr/bin/python

class Sample():
    def __init__(self):
        print "Constructor. Initialize all necessary things here"
        self.__x = 1

    def foo(self):
        print "Class method foo(). Returns value of x"
        return self.__x

    def bar(self):
        print "Class method bar(). Increaments __x by 1"
        self.__x += 1

    @staticmethod
    def deadbeef(y, z):
        print "This is a static method. It should be possible to call this method without an object. It cannot access any non-static class elements"
        return y * z

def main():
    print "Welcome to class sample."
    print Sample.deadbeef(4, 6)

    obj = Sample()
    print obj.foo()
    print obj.bar()
    print obj.foo()


if __name__ == "__main__":
    main()