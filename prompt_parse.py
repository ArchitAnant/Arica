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

def tokenize_install(prompt):
    pkg_name = ""
    words = prompt.split(" ")
    pkg_name = words[len(words)-1]
    return pkg_name


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

def install_pkg(prompt):
    sys_name = sb.run("uname -a",shell=True,capture_output=True).stdout.decode('utf-8')
    pkg_name = tokenize_install(prompt= prompt)
    print("Installing package - {}...".format(pkg_name))
    if ' debian ' in sys_name.lower():
        sb.run("sudo apt-get install {}".format(pkg_name),shell=True)
    elif ' arch ' in sys_name.lower():
        sb.run("sudo pacman -S {}".format(pkg_name),shell=True)
    elif ' fedora ' in sys_name.lower():
        sb.run("sudo dnf install {}".format(pkg_name),shell=True)
    else:
        print("Could not install package. OS not supported.")

def uninstall_pkg(prompt):
    sys_name = sb.run("uname -a",shell=True,capture_output=True).stdout.decode('utf-8')
    pkg_name = tokenize_install(prompt= prompt)
    print("Uninstalling package - {}...".format(pkg_name))
    if ' debian ' in sys_name.lower():
        sb.run("sudo apt-get remove {}".format(pkg_name),shell=True)
    elif ' arch ' in sys_name.lower():
        sb.run("sudo pacman -R {}".format(pkg_name),shell=True)
    elif ' fedora ' in sys_name.lower():
        sb.run("sudo dnf remove {}".format(pkg_name),shell=True)
    else:
        print("Could not uninstall package. OS not supported.")

