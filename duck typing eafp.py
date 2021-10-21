# https://www.youtube.com/watch?v=x3v9zMX1s4s&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=32&ab_channel=CoreySchafer

condition = False

if condition:

    class Duck:

        def quack(self):
            print('quack, quack')

        def fly(self):
            print('flap, flap')

    class Person:

        def quack(self):
            print('I\'m quacking like a duck')

        def fly(self):
            print('I\'m flapping my arms')

    def quack_and_fly(thing):
        # This is rather un-pythonic
        # in duck-typing, we don't care if the object is a duck or not
        # we only care if it can act like a duck
        # it is easier to ask for forgiveness than permission
        if isinstance(thing, Duck):
            thing.quack()
            thing.fly()
        else:
            print('This isn\'t my duck!')

    def quack_and_fly(thing):
        # LYBYL (Non-Pythonic) - look before you leap
        if hasattr(thing, 'quack'):
            if callable(thing.quack):
                thing.quack()

        if hasattr(thing, 'fly'):
            if callable(thing.fly):
                thing.fly()

        print()
        
    def quack_and_fly(thing):
        # EAFP (Pythonic)
        try:
            thing.quack()
            thing.fly()
            thing.bark()
        except AttributeError as e:
            print('I don\'t think this is duck-like ' + str(e))
    
    d = Duck()
    p = Person()

    quack_and_fly(d)
    quack_and_fly(p)

    ###################################
    ## let's look at another example ##

    person = {'name': 'Jess', 'age': 23, 'job': 'progammer'}
    person = {'name:': 'Jess', 'age': 23}

    # LYBL (UnPythonic)
    if 'name' in person and 'age' in person and 'job' in person:
        print('{name}, {age}, {job}'.format(**person))
    else:
        print('missin keys')

    # EAFP (Pythonic)
    try:
        print('{name}, {age}, {job}'.format(**person))
    except KeyError as e:
        print('Missing {} key'.format(e))


    ###################################
    ## let's look at another example ##

    my_list = [1, 2, 3, 4, 5]

    # Non-Pythonic
    if len(my_list) >= 6:
        print(my_list[5])
    else:
        print('index does not exist')

    # Pythonic
    try:
        print(my_list[5])
    except IndexError:
        print('this doesnot quite exist')

    """ 
    So why then?
    1. if you don't expect to encounter a whole lot of errors, it's just faster than to run a bunch of checks.
        This isn't supposed to be a solution for every single problem.
    2. some people argue that it's more readable 
    3. It's faster to crash and catch, than to run a whole bunch of checks
    """

###################################
######## one final example ########

import os
my_file = '/tmp/test.txt'

# Race condition
if os.access(my_file, os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print('file cannot be accessed')

# No Race-Condition
try:
    f = open(my_file)
except IOError as e:
    print('file cannot be accessed')

else:
    with f:
        print(f.read())


""" 
Note that in the first example a sitution could occur,
where the was available when checking access,
but by the time we reach the open() command, it is no longer available
hence it is literally faster and makes more sense to use the EAFP approach here
"""



