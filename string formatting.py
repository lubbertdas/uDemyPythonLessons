person = {'name':'JFK', 'headshots':1.5}

sentence = 'Hi, my name is {}, my name is who, I got headshotted {}'.format(person['name'], person['headshots'])
print(sentence)

sentence = 'Hi, my name is {1}, my name is who, I got headshotted {0}'.format(person['name'], person['headshots'])
print(sentence)

sentence = 'Hi, my name is {0[name]}, my name is who, I got headshotted {0[headshots]}'.format(person)
print(sentence)

text = 'the quick brown fox'
tag = 'b'

sentence = '<{1}>{0}</{1}>'.format(text, tag)
print(sentence)

sentence = 'The {enemy} came down like the {analogie} on the fold'.format(enemy='Slim Shady', analogie='boop')
print(sentence)

### timepoint: 06:40
person = {'name':'what','who':'who','chicky-chicky':'slim shady'}
sentence = 'Hi my name is {name}, my name is {who}, my name is chicky-chicky, {chicky-chicky}'.format(**person)
print(sentence)

for i in range(1,11):
    #print('the value is {}'.format(i))
    #print('the value is {:03}'.format(i))
    #output is: the value is 001 and so forth..
    pass

pi = 3.14159265
sentence = 'Pi is equal to {:.2f}'.format(pi)
# output: Pi is equal to 3.14
print(sentence)

sentence = '1 MB is equal to {:,.2f} byes'.format(1000**2)
# output: 1 MB is equal to 1,000,000.00 byes
print(sentence)

import datetime
# (year, month, day, [hour, minute, seconds])
my_date = datetime.datetime(2016, 10, 28, 11, 35, 00)
# output: 2016-10-28 11:35:00
print(my_date)

# formatting help can be found in python documentation: https://docs.python.org/3/library/datetime.html
sentence = '{:%B %d, %Y}'.format(my_date)
# output: October 28, 2016
print(sentence)

sentence = '{0:%B %d} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)

