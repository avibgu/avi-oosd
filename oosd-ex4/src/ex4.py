## OOP Ex.4

# Put your implementation here


#!/usr/bin/python

# A basic delegate meta-class, based on the code shown in class 10b

from new import instancemethod

def dlgt(cls, method):
    def ret(self, *args):
        method(self.__coll__, *args)
    return instancemethod(ret, None, cls)


class Delegate(type):
    def __init__(cls, name, bases, dct):
        type.__init__(cls, name, bases, dct)
        tgtclass = cls.__tgtclass__
        for name in dir(tgtclass):
            val = getattr(tgtclass, name)
            if name[:2] != '__' and callable(val):
                setattr(cls, name, dlgt(cls, val))
                          
                
class BcastColl(object):

    # list of instances.. initialized to an empty list..
    __coll__ = []
    
    # The collection will delegate all calls to public
    # methods of list to this ?eld.
    # to check if string n is public use:
    # n[:2] != '__'.
    # an instance class of BcastColl should be a delegate of a list.
    # You may use the Delegate meta-class shown in class.
    
    __metaclass__ = Delegate
    __tgtclass__ = list

    def __init__ (self):
    
        #self.__tgt__ = list()

        # Each call to a public method of __instclass__ should be
        # broadcast to the objects in the list _coll__.

        for name in dir(self.__instclass__):
            val = getattr(self.__instclass__, name)
            if name[:2] != '__' and callable(val):
                setattr(cls, name, brdcst(self, val))


def brdcst(cls, method):
    def ret(self, *args):
        # call method for each element in __coll__
        for el in self.__coll__:
            method(el, *args)
    return instancemethod(ret, None, cls)



## Test code

class Employee(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    def giveRaise(self, n):
        self.salary += n

class EmployeeColl(object):
    __metaclass__ = BcastColl
    __instclass__ = Employee

if __name__ == '__main__':
    c = EmployeeColl()
    c.append(Employee('moshe', 1000))
    c.append(Employee('david', 2000))
    test1 = (c.getName() == ['moshe', 'david'])
    c.giveRaise(100)
    test2 = (c.getSalary() == [1100, 2100])
    if test1 and test2:
        print 'ok'
    else:
        print 'fail'
