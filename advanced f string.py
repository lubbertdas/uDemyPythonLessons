# https://www.youtube.com/watch?v=nghuHvKLhJA&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=35&ab_channel=CoreySchafer

condition = False

if condition:
    first_name = "John F."
    last_name = "Kennedy"

    # the old method
    sentence = 'my name is {}{}.'.format(first_name, last_name)
    print(sentence)

    # the new method
    sentence = f'my name is {first_name} {last_name}.'
    print(sentence)

    # we can also put a method inside
    sentence = f'my name is {first_name.upper()} {last_name.upper()}.'

    person = {'name':'john', 'age':47}

    # once again, old method with dictionary
    sentence = 'my name is {} {}.'.format(person['name'], person['age'])

    # new method with dictionary. note that using single quotes would have conflicted with the string's quotes.
    sentence = f'my name is {person["name"]} {person["age"]}.'
    print(sentence)

    # anothe demonstration of calculates
    calculation = f'4 times 11 is equal to {11*4}'
    print(calculation)

    a = 20
    b = 33
    calculation = f'{a} times {b} is equal to {a*b}'
    print(calculation)

    for n in range(1, 11):
        # demonstration of padding to two digits
        print(f'the value is {n:02}')


    pi = 3.14159265
    # presenting up to 4 floating point value
    sentence = f'Pi is {pi:.4f}'
    print(sentence)

    # formatting dates
    from datetime import datetime
    birthday = datetime(1990, 1, 1)
    sentence = f'Jack\'s birthday is on {birthday:%B %d, %Y}' 
    print(sentence)