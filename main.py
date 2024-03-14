from load_model import chat as c
import utills
import networking
import hardware

prompt = input("Enter your query: ")
tag = c(prompt)

if tag == 'FILE_CREATION':
    utills.file_creation(prompt=prompt)

elif tag == 'DIR_CREATION':
    utills.dir_creation(prompt=prompt)

elif tag == 'FILE_DELETION':
    utills.file_deletion(prompt=prompt)

elif tag == 'DIR_DELETION':
    utills.dir_deletion(prompt=prompt)

elif tag == 'COPY_FILE':
    utills.copy_file(prompt=prompt)

elif tag == 'INSTALL_PKG':
    utills.install_pkg(prompt=prompt)

elif tag == 'UNINSTALL_PKG':
    utills.uninstall_pkg(prompt=prompt)

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

elif tag == 'PCI_SHOW':
    hardware.list_pci()

elif tag == 'USB_SHOW':
    hardware.list_usb()

elif tag == 'SHOW_FILE_CONTENTS':
    utills.cat_file(prompt=prompt)

elif tag == 'BLOCK_DEVICES':
    hardware.list_blk()

elif tag == 'LIST_SERVICES':
    utills.list_services()

elif tag == 'COMPRESS_FILE':
    utills.comporess_file()