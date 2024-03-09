import subprocess as sb
from nltk.tokenize import word_tokenize

def tokenize_f(prompt):
    file_name = ""
    words =  prompt.split(" ")
    file_name = words[len(words)-1]
    return file_name

def tokenize_copy(prompt):
    from_file = ""
    to_file = ""
    words = prompt.split(" ")
    if 'to' in words:
        to_index = words.index('to')
        from_file = words[to_index-1]
        to_file = words[to_index+1]

    return [from_file, to_file]

def file_creation(prompt):
    print("Creating file...")
    file_name = tokenize_f(prompt= prompt)
    sb.run("touch {}".format(file_name),shell=True)

def dir_creation(prompt):
    print("Creating directory...")
    dir_name = tokenize_f(prompt= prompt)
    sb.run("mkdir {}".format(dir_name),shell=True)

def file_deletion(prompt):
    print("Deleting file...")
    file_name = tokenize_f(prompt= prompt)
    sb.run("rm {}".format(file_name),shell=True)

def dir_deletion(prompt):
    print("Deleting directory...")
    dir_name = tokenize_f(prompt= prompt)
    sb.run("rmdir {}".format(dir_name),shell=True)

def copy_file(prompt):
    print("Copying file...")
    from_file,to_file = tokenize_copy(prompt= prompt)
    sb.run("cp {} {}".format(from_file,to_file),shell=True)