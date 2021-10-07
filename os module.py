import os

state = False
if state: 

    # prints all attributes and methods we have access to within a module, this is not just strictly for the OS module
    print(dir(os))

    # get current working directiory
    print(os.getcwd())

    # change working directory
    os.chdir('/Users/ranka/Desktop') #could also use: C:/Users/ranka/Desktop
    print(os.getcwd())

    # list directories in current working dir
    print(os.listdir())

    # create mkdir - make dir
    os.mkdir('drrrr')

    # if we want to create a directroy that is several levels deep, for instance:
    os.makedirs('drrrr/hurrrr/wirrrr')

    # remove the last dir specificed in path, examples:
    os.rmdir('drrrr') # deletes drrr and all sub-folders
    os.rmdir('drrrr/hurrrr/wirrrr') # deletes only wirrrr

    # rename file, 1st argument original name, 2nd argument new name
    os.rename('test.txt', 'demo.txt')

    # get info about file
    print(os.stat('demo.txt'))
    # output : os.stat_result(st_mode=33206, st_ino=353814045725294901, st_dev=342707406, 
    #                         st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1633415552, st_mtime=1633415552, st_ctime=1633415552)
    # st_size - 0 bytes
    # st_mtime - last modification time

    # can also print specific data like so:
    print(os.stat('demo.txt').st_size)
    timestamp = os.stat('demo.txt').st_mtime
    from datetime import datetime
    # convert timestamp to display time
    print(datetime.fromtimestamp(timestamp))

    # os.walk() maps out a given dir and its subfolders
    # generates a touple of three values (path, dirs within, files within), as it's walking the directory tree
    # traverses from the top down
    for dirpath, dirnames, filenames in os.walk('/Users/ranka/Desktop'):
        print('Current path: {} \n Sub-dirs: {} \n Files: {} \n'.format(dirpath, dirnames, filenames))
        pass

    # get environment variables
    os.environ
    # get just specific env vars
    print(os.environ.get('JAVA_HOME'))

    # lets try to get a file path
    file_path = os.environ.get('APPDATA') + 'test.txt'
    print(file_path)
    # output: C:\Users\ranka\AppData\Roamingtest.txt

    # We won't always get a slash at the end of the path, so what do we do? use the path module
    file_path = os.path.join(os.environ.get('APPDATA'), 'test.txt')
    print(file_path)
    # output: C:\Users\ranka\AppData\Roaming\test.txt

    # get the basename of a path, doesn't matter if it exists or not, it treats it as a string
    print(os.path.basename('/tmp/test.txt'))
    # output: test.txt

    # get only directory name
    print(os.path.dirname('/tmp/test.txt'))
    # output: /tmp

    # get path as seperate arguments
    print(os.path.split('/tmp/test.txt'))
    # output: ('/tmp', 'test.txt')

    # check if path exists
    print(os.path.exists('/tmp/test.txt'))
    # output: False

    # paths won't always have endings to indicate if we're handling a file or a folder, so we can use these two methods
    print(os.path.isfile('/tmp/test'))
    print(os.path.isdir('/tmp/test'))

    # splits file path from its extension
    print(os.path.splitext('/tmp/test.txt'))
    # output: ('/tmp/test', '.txt')

    # see all methods and attributes available within os.path module
    print(dir(os.path))




