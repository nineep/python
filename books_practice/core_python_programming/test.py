#!/usr/bin/env python

if user.cmd == 'create':
    action = 'create item'

elif user.cmd == 'delete':
    action = 'delete item'

elif user.cmd == 'update':
    action = 'update item'

else:
    action = 'invalid choice... try again!'


if user.cmd in ('create', 'delete', 'update'):
    action = '%s item' % user.cmd
else:
    action = 'invalid choice... try again!'


msgs = {'create': 'create item',
        'delete': 'delete item',
        'update': 'update item'}
default = 'invalid choice... try again!'
action = msgs.get(user.cmd, default)

valid = False
count = 3
while count > 0:
    input = raw_input("enter password")
    # check for valid passwd
    for eachPasswd in passwdList:
        if input == eachPasswd:
            valid = True
            break
    if not valid:       #(or valid == 0)
        print "invalid input"
        count -= 1
        continue
    else:
        break


from random import randint

def odd(n):
    return n % 2

allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))
print filter(odd, allNums)



def map(func, seq):
    mapped_seq = []
    for eachItem in seq:
        mapped_seq.append(func(eachItem))
    return mapped_seq
map ((lambda x: x+2), [0, 1, 2, 3, 4, 5])

from cli4ovf import import cli4ovf
#command line interface utility function
def cli_util():
    pass
#overly massive handlers for the command line interface
def omh4cli():
    :
    cli4ovf()
    :
    omh4cli()

class AddrBookEntry(object):
    'address book entry class'
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print 'Created instance fo:', self.name
    def updatePhone(self, newph):
        self.phone = newph
        print 'Updated phone# for:', self.name

john = AddrBookEntry('Hohn Doe', '408-555-1212')
jane = AddrBookEntry('Jane Doe', '650-555-1212')

class EmplAddrBookEntry(AddrBookEntry):
    'Employee Address Book Entry class'
    def __init__(self, nm, ph, id, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em

    def updateEmail(self, newem):
        self.email = newem
        print 'Update e-mail address for:', self.name

John = EmplAddrBookEntry('John Doe', '408-555-1212', 42, 'john@spam.doe')


class NewAddrBookEntry(object):
    'new address book entry class'
    def __init__(self, nm, ph):
        self.name = Name(nm)
        self.phone = Phone(ph)
        print 'Created instance for:', self.name

class Parent(object):
    def parentMethod(self):
        print 'calling child method'

class Child(Parent):
    def childMethod(self):
        print 'calling child method'

class RoundFloat(float):
    def __new__(cls, val):
        return float.__new__(cls, round(val, 2))

class RoundFloat(float):
    def __new__(cls, val):
        return super(RoundFloat, cls).__new__(cls, round(val, 2))

def foo(data):
    if isinstance(data, int):
        print 'you entered an integer'
    elif isinstance(data, str):
        print 'you entered a string'
    else:
        raise TypeError, 'only integers or strings!'

