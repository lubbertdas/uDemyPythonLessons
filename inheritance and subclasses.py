# https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=43&ab_channel=CoreySchafer

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

class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_language):
        #calling the Employee init to initialize the developer class
        super().__init__(first, last, pay)
        #could also be written as, but isn't as maintainable
        Employee.__init__(self, first, last, pay)
        self.prog_language = prog_language        
        pass

    pass

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('John F.', 'Kennedy', 5000, 'Python')
dev_2 = Developer('Robert F.', 'Kennedy', 6000, 'Java')
mang = Manager('Abe', 'Linc', 10000, [dev_1])

condition = False

if condition:
    dev_1.apply_raise()
    dev_2.apply_raise()

    print(f'Apply John Raise: {dev_1.pay}')
    print(f'Apply John Raise: {dev_2.pay}')

    # prints out class details
    print(help(Developer))

    print(dev_1.email)
    print(dev_1.prog_language)

    mang.add_employee(dev_2)
    mang.print_employees()

    # check if manager is an instance of manager
    print(isinstance(mang, Manager)) # True
    print(isinstance(mang, Employee)) # True
    print(isinstance(mang, Developer)) # False
    # check if class inherits from another class
    print(issubclass(Developer, Employee)) # True
    print(issubclass(Manager, Employee)) # True
    print(issubclass(Employee, Employee)) # True
    print(issubclass(Manager, Developer)) # False

