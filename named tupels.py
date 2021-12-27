from collections import namedtuple

# https://www.youtube.com/watch?v=GfxJYp9_nJA

condition = False
if condition:
    # a nametuple is like a regular tuple, only more readable, it's a lightweight object

    # an RGB value for example
    color = (55, 155, 255)
    # this isn't very clear right now, it's not necessarily obvious that this is RGB
    print(color[0])

    # suppose we defined a dictionary instead
    color = {'red':55, 'green':155, 'blue': 255}
    print(color['red'])
    # so why not use a dictionary? well maybe we used a tuple for a reason
    # tuples are for instance immutabile, meaning you can't them once they've been initialized
    # also dictionaries require a little bit more typing which is tiresome or something
    # a named tuple is a good compremise between readiblity and the functionality of a tuple

Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(red=55, green=155, blue=255)
# could also be written like so:
color = Color(55, 155, 255)
# but also like this
color = Color(blue = 1, green = 2, red = 3)

print(color)
#returns: Color(red=3, green=2, blue=1)

print(color.red)
#returns: 3
