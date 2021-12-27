# https://www.youtube.com/watch?v=jCzT9XFZ5bw

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    # added thing property decorator allows us to access this method as if it were a property
    # this is a getter method, it doesn't allow us to set
    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    # this method is now defined as the fullname setter
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # this method would be run whenever we delete the fullname property
    @fullname.deleter
    def fullname(self):
        #print('deleted name!')
        self.first = None
        self.last = None

emp_1 = Employee('John F.', 'Kennedy')

emp_1.first = "Jim"
emp_1.fullname = 'Jerry Seinfelf'

print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.fullname)