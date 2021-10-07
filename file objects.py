# https://www.youtube.com/watch?v=Uh2ebFW8OYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=25&ab_channel=CoreySchafer #

statement = False

if statement:
    # r - read only
    # w - rewrite
    # a - append
    # r+ - read and write
    f = open('test.txt', 'r')

    f = open('test.txt', 'r')
    #print file name 
    print(f.name)
    # if we don't close the file, we could run into leaks
    f.close()

    # using a context manager, once we exit this block of code, it will close the file for us, whether we added close() or not
    with open('test.txt', 'r') as f:
        print(f.name)
        f.close()

    # using a context manager, once we exit this block of code, it will close the file for us, whether we added close() or not
    with open('test.txt', 'r') as f:
        pass

    # we still have access to the variable outside of the code block, but the file will be closed, we cannot continue reading
    print(f.closed)
    # output: true

    with open('test.txt', 'r') as f:
        # read the file contents
        f_contents = f.read()
        print(f_contents)

    with open('test.txt', 'r') as f:
        # what if the file is very large and we do not wish to read the entire file
        f_contents = f.readlines()
        print(f_contents)
        # output of two lines file, returns a list: ['What hath God wrought?\n', '?thguorw doG htah tahW']

    with open('test.txt', 'r') as f:
        # could also just read a single line
        # every time we run the readline() command, it will run the next line
        # essentially this is a stream that we're advancing over
        f_contents = f.readline()
        print(f_contents)

    with open('test.txt', 'r') as f:
        # so if we'll try to read a large file all at once, we might run out of memory
        # instead we'll iterate over the lines in the file
        for line in f:
            # we add the end argument, because each line already ends in \n
            print(line, end='')

    with open('test.txt', 'r') as f:
        # we can pass how many characters we wish to read as the first argument, in this case we'll read 5 characters
        # once we reach the end of a file, we receive an empty string
        f_contents = f.read(5)
        print(f_contents)

    with open('test.txt', 'r') as f:
        size_to_read = 5
        # create a loop that reads 5 characters at a time until it reaches the end
        # we use f.tell() to print our current position each time we print
        f_contents = f.read(size_to_read)
        while len(f_contents) > 0:
            print(f_contents, end=str(f.tell()))
            f_contents = f.read(size_to_read)

    with open('test.txt', 'r') as f:
        size_to_read = 5
        f_contents = f.read(size_to_read)
        print(f_contents, end='')

        # jump to a character position in the file, in this case the start
        f.seek(0)

        f_contents = f.read(size_to_read)
        print(f_contents, end='')

    # if the file doesn't exist already, w will create it, if it does exist, it will overwrite it
    # if don't want to overwrite, we'll use 'a' for append
    with open('test2.txt', 'w') as f:
        # just by running the code, the file is created
        pass

    with open('test2.txt', 'w') as f:
        # write TestTest
        f.write('Test')
        f.write('Test')

    with open('test2.txt', 'w') as f:
        # Write Test and then overwrite the first 4 letters
        f.write('TestPass')
        f.seek(0)
        f.write('tseT')
        pass

    # a demonstration of copying one file to a new one
    with open('test.txt', 'r') as rf:
        with open('test_copy.txt', 'w') as wf:
            for line in rf:
                wf.write(line)
            pass
        pass

    # now let's try to copy a puppy
    # we're gonna have to open the files in binary mode, so as arguments in open, we write: rb, wb
    with open('puppy.jpg', 'rb') as rf:
        with open('puppy_copy.jpg', 'wb') as wf:
            for line in rf:
                wf.write(line)
            pass
        pass

# now let's redo this, but instead of lines, we'll read chunks
with open('puppy.jpg', 'rb') as rf:
    with open('puppy_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk):
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
    pass


    

