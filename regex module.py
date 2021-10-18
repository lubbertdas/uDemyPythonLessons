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

cat
mat
pat
bat
'''

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
jacky@whitehouse.gov.uk
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
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

    # match the phone numbers pattern
    # note we didn't haveto escape the dot in the character set
    pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')

    ############################################################

    # match the phone numbers pattern and extract it from a file
    pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')

    with open('data.txt', 'r', encoding='utf-8') as f:
        contents = f.read()

        matches = pattern.finditer(contents)

        for match in matches:
            print(match)

    ############################################################

    # if we only want to match numbers beginning with 800 or 900
    pattern = re.compile(r'[98][0]{2}[.-]\d{3}[.-]\d{4}')

    matches = pattern.finditer(text_to_search)

    for match in matches:
            print(match)

    ############################################################

    # if we only want to match digits between 1 and 5, we use the dash
    pattern = re.compile(r'[1-5]')
    # if we only want to match letters between a and z, we use the dash
    pattern = re.compile(r'[a-z]')
    # if we only want to match letters between a and z lowercase and uppercase, we use the dash
    pattern = re.compile(r'[a-zA-Z]')

    # using a caret means to search for anything that DOESN'T fit the characters specified
    pattern = re.compile(r'[^a-zA-Z]')

    # match any single character which isn't a 'b', followed by 'at'
    pattern = re.compile(r'[^b]at')

    # get all first names that begin with Mr
    pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

    # using a group to match Mr, Mrs, Ms
    pattern = re.compile(r'M(r|rs|s)\.?\s[A-Z]\w*')

    # my first solution to match email addresses. allows illegal characters however
    pattern = re.compile(r'.+@.+\..(\w+|\w+.\w+)')

    # coreys solution
    pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+.(com|edu|net)+')

    # another regex example for email address
    pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

    # get all urls. note the usage of ? to signify the s may or may not appear
    pattern = re.compile(r'https?://[a-zA-Z-.]+\.[a-zA-Z.]+')

    # coreys solution for getting URLS
    pattern = re.compile(r'https?://(www\.)?\w+\.\w+')

    ############################################################

    # to capture the sections we want, we can surround them by parenthasis
    # we can access the group in the matches
    pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

    matches = pattern.finditer(urls)

    for match in matches:
        # group 0 is the entire match
        # z.B. https://www.google.com
        print(match.group(0))

        # group 2 is our domain name
        # group 3 is the ending, com or gov
        print(match.group(2) + match.group(3))

    ############################################################

    pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

    # use our pattern to subtitute all our matches with the desired groups
    # in this case we're replacing the matches with groups 2 and 3
    subbed_urls = pattern.sub(r'\2\3', urls)

    ''' output: 
    google.com
    coreyms.com
    youtube.com
    nasa.gov
    '''

    print(subbed_urls)

    ############################################################

    # using pattern.findall() we would only get the group we defined - Mr/Mrs/Ms
    # if there are no groups, it would return the result in a touple of string
    pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s[A-Z]\w*')
    matches = pattern.findall(text_to_search)

    for match in matches:
        print(match)

    # pattern.match will only return a result if the string starts with what we're looking for, otherwise returns None
    pattern = re.compile(r'Start')
    # if we tried this pattern = re.compile(r'sentence'), we'll get nothing, despite "sentence" occuring in the string
    matches = pattern.match(sentence)
    print(matches)
    # prints Start

    # pattern.search if we want to search the entire string, will only return the first result it finds
    pattern = re.compile(r'sentence')
    matches = pattern.search(sentence)
    print(matches)

    # FLAGS
    # we can use flags to make our life a little easier
    # say we want to search for a string with alternating lower\uppercase characters
    pattern = re.compile(r'start', re.IGNORECASE)
    # could be written like this just as well
    pattern = re.compile(r'start', re.I)

    # there is also a multi-line flag that allows us to use caret, 
    # so we can search for the end or beginning of each line
    # there is also a verbose flag, we allows to add white spaces and comments directly within the pattern, to make it easier to understand

pattern = re.compile(r'start', re.I)
matches = pattern.search(sentence)
print(matches)