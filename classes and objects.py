# Tutorial link: https://www.youtube.com/watch?v=ZDa-Z5JzLYM&ab_channel=CoreySchafer

class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        pass

    def get_name(self):
        return ('{} {}'.format(self.first, self.last))    

# using the parenthasis indicates Employee is expected to inherit from another class, in this case - Person
class Employee(Person):

    # regular methods automaticaly pass the instance as first argument, which we name self
    # classmethods pass the class as the first argument, we name it cls
    # static methods pass jack shit, neither instance or class, just like regular functions

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@erlington.gov'
        pass

    # example of creating an _alternative constructor_
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    def get_details(self):
        return ('{} {}: {}'.format(self.first, self.last, self.email))

    # sets raise_amount for all instances
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(date):
        if (date.weekday() == 5) or (date.weekday() == 6):
            return False
        else:
            return True
        pass

    pass

emp_1 = Employee("john", "kennedy", 500)
emp_2 = Employee("jacky", "boubier", 250)

print(emp_1.get_name())
print(Employee.get_details(emp_2))

if False:
    print(Employee.raise_amount)
    Employee.set_raise_amt(1.5)
    print(Employee.raise_amount)

new_emp_1_str = 'Bobby-Kennedy-125'
new_emp_2_str = 'Lee-Harvey-105'
new_emp_1 = Employee.from_string(new_emp_1_str)
new_emp_2 = Employee.from_string(new_emp_2_str)

print(Employee.get_details(new_emp_2))

import datetime
my_date = datetime.date(2023, 10, 28)
print(Employee.is_workday(my_date))
