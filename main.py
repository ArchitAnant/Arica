from load_model import chat as c
import prompt_parse
import networking

prompt = input("Enter your query: ")
tag = c(prompt)

if tag == 'FILE_CREATION':
    prompt_parse.file_creation(prompt=prompt)

elif tag == 'DIR_CREATION':
    prompt_parse.dir_creation(prompt=prompt)

elif tag == 'FILE_DELETION':
    prompt_parse.file_deletion(prompt=prompt)

elif tag == 'DIR_DELETION':
    prompt_parse.dir_deletion(prompt=prompt)

elif tag == 'COPY_FILE':
    prompt_parse.copy_file(prompt=prompt)

elif tag == 'INSTALL_PKG':
    prompt_parse.install_pkg(prompt=prompt)

elif tag == 'UNINSTALL_PKG':
    prompt_parse.uninstall_pkg(prompt=prompt)

elif tag == 'SEND_FILE':
    networking.send_file()

elif tag == 'RECIEVE_FILE':
    networking.receive_file()

elif tag == 'IP_ADDRESS':
    networking.get_ip()

elif tag == 'SCAN_NETWORK':
    networking.scan()

elif tag == 'IS_PKG_INSTALLED':
    networking.check_wrapper(prompt=prompt)
elif tag == 'CHECK_INTERNET':
    networking.check_internet()