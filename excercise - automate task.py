import os

## this script's purpose to rename a bunch of files

os.chdir('/Users/ranka/Desktop/testpoop')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)

    new_name = file_name.split('(')[0]
    number = file_name.split('(')[1]
    number = number.split(')')[0]

    new_name = new_name.strip()
    number = number.zfill(2)

    new_name = '{} - {}{}'.format(number, new_name, file_ext)

    os.rename(f, new_name)

    #print(new_name)