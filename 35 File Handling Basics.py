##### API ####

def read(file_path):
    f = open(file_path)
    return f.read()

# attempting to write to a file which doesn't exist, will create a new file#
def write(file_path, text):
    f = open(file_path, "w")
    f.write(text)

def append(file_path, text):
    f = open(file_path, "a")
    f.write(text)

def append_new_line(file_path, text):
    text = "\n" + text
    append(file_path, text)

def create(file_path):
    f = open(file_path, "x")    

def read_and_execute(file_path):
    code = read(file_path)
    exec(code, globals())


file_path = "file.txt"

########### EXAMPLES ###########

def writing_example():
    old_text = "What hath God wrought?"
    new_text = ""
    for c in (reversed(old_text)):
        new_text = new_text + c

    write(file_path, old_text)
    append_new_line(file_path, new_text)
    file_content = read(file_path)
    print(file_content)

# will return: FileExistsError: [Errno 17] File exists: 'file.txt'
def failed_create_example():
    create(file_path)

def create_file_example():
    create("C:/Users/ranka/what.txt")

def code_execution_example():
    write(file_path, "print('hello world')")
    code = read(file_path)
    exec(code)

def run_requests():
    read_and_execute("31 Http Requests to Api.py")

##### RUN #####

create_file_example()

