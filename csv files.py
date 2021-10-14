# https://www.youtube.com/watch?v=q5uM4VKywbA&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=28&ab_channel=CoreySchafer

import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    condition = False

    if condition:

        # print all lines
        for line in csv_reader:
            print(line)

        # print line data at index
        for line in csv_reader:
            print(line[0])

        # to jump over the first line, or just advance a line
        next(csv_reader)

    
        with open('new_names.csv', 'w') as new_file:
            # we decided to write a new file, and use '-' as a delimiter. if we hadn't defined, it would've been ',' probably
            # because csv stands for comma seperated vavavooom
            csv_writer = csv.writer(new_file, delimiter='-')
            # the csv writer would put quotation marks on value which contain the delimiter, to know to read the whole value

            # write each line from the old file to the new file
            for line in csv_reader:
                csv_writer.writerow(line)

        # newline='' is to prevent an extra line being added after each line
        with open('new_names.csv', 'w', newline='') as new_file:
            # let's use tab as a delimiter instead
            csv_writer = csv.writer(new_file, delimiter='\t')

            for line in csv_reader:
                csv_writer.writerow(line)


# let's start again, now with the new file
with open('new_names.csv', 'r') as csv_file:

    condition = False

    if condition:
        # define the delimiter to help with formatting, it isn't strictly necessary
        csv_reader = csv.reader(csv_file, delimiter='\t')

        for line in csv_reader:
            print(line)


with open('names.csv', 'r') as csv_file:
    # let's demonstrate the dictionary reader feature
    csv_reader = csv.DictReader(csv_file)

    condition = False
    
    if condition:
        for line in csv_reader:
            # output example: {'first_name': 'Travis', 'last_name': 'Arnold', 'email': 'travisarnold@bogusemail.com'}
            # note that the field names now serve as keys
            print(line)

            # could also do:
            print(line['first_name'])
    
    with open('new_names.csv', 'w', newline='') as new_file:

        condition = False
    
        if condition:
            # in order to use the DictWriter, we have to define the field name
            field_names = ['first_name', 'last_name', 'email']

            # we pass the field_names list as the second argument
            csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter='\t')

            # before writing the actual data, we can write out the headers
            csv_writer.writeheader()

            for line in csv_reader:
                csv_writer.writerow(line)

        # this time let's only print first and last name fields
        field_names = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter='\t')
        csv_writer.writeheader()

        for line in csv_reader:
            # we specify to write the email from the line
            del line['email']
            csv_writer.writerow(line)




