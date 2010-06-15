#!/usr/bin/python

# A basic delegate meta-class, based on the code shown in class 10b

from new import instancemethod

def dlgt(cls, method):
    def ret(self, *args):
        method(self.__tgt__, *args)
    return instancemethod(ret, None, cls)

class Delegate(type):
    def __init__(cls, name, bases, dct):
        type.__init__(cls, name, bases, dct)
        tgtclass = cls.__tgtclass__
        for name in dir(tgtclass):
            val = getattr(tgtclass, name)
            if name[:2] != '__' and callable(val):
                setattr(cls, name, dlgt(cls, val))

## Test code

def clsname(self):
    return self.__class__.__name__

class A(object):
    def bar(self):
        print clsname(self), 'bar'
    def baz(self):
        print clsname(self), 'baz'

class B(object):
    __metaclass__ = Delegate
    __tgtclass__ = A
    def __init__(self, tgt):
        self.__tgt__ = tgt
    def boo(self):
        print clsname(self), 'boo'

if __name__ == '__main__':
    b = B(A())
    b.bar()
    b.baz()
    b.boo()
    