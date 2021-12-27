# https://www.youtube.com/watch?v=3ohzBxoFHAY

# by defining our special methods, we will be able to define our own behavior for default methods such as print, addition, etc.
# these default methods are always surrounded by underscores ('_'), some people call them dunder

class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@erlington.gov'
        pass

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # repr is meant to be unambigious definition of the object, used for debugging by developers
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # str is meant to be a readable representation of an object, displayed to the end user
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('John F.', 'Kennedy', 5000)
emp_2 = Employee('Robert F.', 'Kennedy', 6000)

condition = False

if condition:
    # when only repr is overriden, the output is: Employee('John F.', 'Kennedy', '5000')
    print(emp_1)

    # when print is overriden, the output is: John F. Kennedy - John F..Kennedy@erlington.gov
    print(emp_1)
    
    # we could access the methods specifically by doing this:
    print(repr(emp_1))
    print(str(emp_1))

    # which would be the same as doing
    print(emp_1.__repr__())
    print(emp_1.__str__())

    # we could also override methods used for arithmetics
    # z.B., these are the default functions for integers and strings
    print(int.__add__(1, 2))
    print(str.__add__('a', 'b'))
    # once we've overriden the __add__ method, it can perform this operation
    print(emp_1 + emp_2)

    # overriden __len__ method
    print(len(emp_1))




