# https://www.youtube.com/watch?v=FsAPt_9Bf3U&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=37&ab_channel=CoreySchafer

condition = False

if condition:

    # we can pass functions as arguments
    # we can return functions
    # we can assign function to variables
    # let's start by a recap of closures

    def outer_function():
        message = 'Lola'

        def inner_function():
            print(message)

        # if we exceute the inner_function, it would simply print hi
        # return inner_function()
        # we can however not execute it, and just return it
        return inner_function

    # we save the function our function, then execute it
    my_func = outer_function()
    my_func()

    #################################
    # let's add msg as an argument
    def outer_function(msg):
            def inner_function():
                print(msg)
            return inner_function

    hi_func = outer_function('lala')
    bye_func = outer_function('lolo')
    hi_func() # prints lala
    bye_func() # prints lolo

    #################################
    # let's complicate things just for fun
    def decorator_function(original_function):
            def wrapper_function():
                return original_function
            return wrapper_function

    def display():
        print('display function says hi')

    decorated_display = decorator_function(display)
    decorated_display()

    #################################
    # now let's unpack the inner shit
    def decorator_function(original_function):
            def wrapper_function():
                return original_function
            return wrapper_function

    def display():
        print('display function says hi')

    decorated_display = decorator_function(display)
    decorated_inner_function = decorated_display()
    decorated_inner_function()

    #################################
    # printing out function name before calling it 
    def decorator_function(original_function):
            def wrapper_function():
                print('wrapper execute this before {}'.format(original_function.__name__))
                return original_function()
            return wrapper_function

    def display():
        print('display function says hi')

    decorated_display = decorator_function(display)
    decorated_display()
    # output:
    # wrapper execute this before display
    # display function says hi

    #################################
    # let's look at decotrator syntax (@)
    def decorator_function(original_function):
            def wrapper_function():
                print('wrapper execute this before {}'.format(original_function.__name__))
                return original_function()
            return wrapper_function

    # using this syntax, display() would have the decotrator_function() functionality added on
    @decorator_function
    def display():
        print('display function says hi')

    display() 
    # output:
    # wrapper execute this before display
    # display function says hi

    #################################
    # now let's pass arguments
    def decorator_function(original_function):
            # *args and **kwargs can be named whatever we want, 
            # but by convention they are written this way
            def wrapper_function(*args, **kwargs):
                print('wrapper execute this before {}'.format(original_function.__name__))
                return original_function(*args, **kwargs)
            return wrapper_function

    @decorator_function
    def display():
        print('display function says hi')

    @decorator_function
    def display_info(name, age):
        print('display_info ran with arguments ({}, {})'.format(name, age))

    display()
    display_info('lo', 'la') 
    # output for both:
    """ 
    wrapper execute this before display
    display function says hi
    wrapper execute this before display_info
    display_info ran with arguments (lo, la)
    """

    #################################
    # let's demonstrate another syntax we might encounter
    # sometimes classes are used as decorators, instead of functions
    # we don't have to do the '(object)' thing, i dunno what it's for
    class decorator_class(object):
        def __init__(self, original_function):
            self.original_function = original_function

        # this would be automatically executed when calling the original function
        def __call__(self, *args, **kwargs):
            print('call method executed this before {}'.format(self.original_function.__name__))
            return self.original_function(*args, **kwargs)

    @decorator_class
    def display():
        print('display function says hi')

    @decorator_class
    def display_info(name, age):
        print('display_info ran with arguments ({}, {})'.format(name, age))

    display()
    display_info('lo','la')

    #################################
    # let's look at some practical examples
    # one of the more common uses of decorators is logging
    # we want to know how many times a function is called and how long it takes to run
    def my_logger(orig_func):
        import logging
        logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

        def wrapper(*args, **kwargs):
            logging.info(
                'Ran with args: {}, and kwargs {}'.format(args, kwargs))
            return orig_func(*args, **kwargs)
        
        return wrapper

    def my_timer(orig_func):
        import time
        def wrapper(*args, **kwargs):
            t1 = time.time()
            result = orig_func(*args, **kwargs)
            t2 = time.time() - t1
            print('{} ran in: {} sec'.format(orig_func.__name__, t2))

        return wrapper

    @my_logger
    def display():
        print('display function says hi')

    # in this case the decorator allows us to maintain a unified log by easily applying it to whatever function we find relevant
    @my_timer
    def display_info(name, age):
        print('display_info ran with arguments ({}, {})'.format(name, age))

    display_info('Bebs', 'Bergers') 

    #################################
    # we can also chain several decorators, this would, however, lead to some unexpected behavior
    # putting my_logger before my_timer will lead to logging of my_timer.wrapper function
    # putting my_timer before my_logger will lead to measuring the time my_logger.wrapper ran
    @my_timer
    @my_logger
    def display_info(name, age):
        print('display_info ran with arguments ({}, {})'.format(name, age))

    # it would be equivalent to doing this
    display_info = my_logger(my_timer(display_info))

    # fittingly, the output of the next command would be: wrapper
    print(display_info.__name__)

    #################################
    # so how do we resolve the issue of chaining decorators? using functools
    # we added the @wraps decorator to each wrapper. Confusing? not at all
    from functools import wraps
    def my_logger(orig_func):
        import logging
        logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

        @wraps(orig_func)
        def wrapper(*args, **kwargs):
            logging.info(
                'Ran with args: {}, and kwargs {}'.format(args, kwargs))
            return orig_func(*args, **kwargs)
        
        return wrapper

    def my_timer(orig_func):
        import time
        @wraps(orig_func)
        def wrapper(*args, **kwargs):
            t1 = time.time()
            result = orig_func(*args, **kwargs)
            t2 = time.time() - t1
            print('{} ran in: {} sec'.format(orig_func.__name__, t2))

        return wrapper

    @my_logger
    @my_timer
    def display_info(name, age):
        print('display_info ran with arguments ({}, {})'.format(name, age))

    display_info('Hank', '45')