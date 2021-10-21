# https://www.youtube.com/watch?v=NIWwJbo-9_8&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=31&ab_channel=CoreySchafer


""" 
try:
    pass
except Exception:
    pass
else:
    pass
finally:
    pass 
"""

from typing import final


condition = False
if condition:
    try:
        f = open('data.txt', encoding='UTF-8')
        # var = bad_var
        pass
    # note to always put the more specific Execptions ahead of the generall ones, 
    # otherwise you'll never reach the specific exception.
    # For instance Exception, which is I guess the most generall, would otherwise have caught everything
    except FileNotFoundError as e:
        print('file not fond: ' + str(e))
        pass
    except Exception as e:
        print('sorry, something went: ' + str(e) + ' eewww')
    # The else-clause runs code when an exception was not encountered
    else:
        print(f.readline() + 'is this the real life? ')
        f.close()
        pass
    # regardless of whatever happened earlier, let's do this
    finally:
        print('Finally, it has happened to me, right in front of my face')
        pass


# suppose we want to raise our own exception
try:
    f = open('data.txt', encoding='UTF-8')
    if (f.name == 'data.txt'):
        raise Exception
        pass
except Exception as e:
    print('eexxccppeettiioonn: ' + str(e))
    pass