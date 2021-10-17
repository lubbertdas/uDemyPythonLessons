# https://www.youtube.com/watch?v=K8L6KVGG-7o&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=30&ab_channel=CoreySchafer

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

condition = False

if condition:

    # raw string in python is a string prefixed with an r. This tells python not to handle back slashes usw.
    print('\tTab') # would print '  Tab'
    print(r'\tTab') #would print '\tTab'

    # we define a pattern, it would literally only look for 'abc' in smallcase in this order
    pattern = re.compile(r'abc')

    matches = pattern.finditer(text_to_search)

    for match in matches:
        print(match)
        # output: <re.Match object; span=(1, 4), match='abc'>
        # span are the indexes of the value
        
    # let's plug those values in
    print(text_to_search[1:4])

    ###

    # let's say we want to search for period
    # because it is a special character, we have to escape it, using a back slash
    pattern = re.compile(r'\.')

    # suppose we want to find that email address, we would write it like so
    pattern = re.compile(r'coreyms\.com')

    # looking for a string that starts with a
    pattern = re.compile(r'^a')

    # would return the location of the end of the string
    pattern = re.compile(r'$')

# would return the location of the end of the string
pattern = re.compile(r'$')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
