from load_model import chat as c
import utills
import networking
import hardware
from argparse import ArgumentParser

def main(args):
    tag = c(args.query)

    if tag == 'FILE_CREATION':
        utills.file_creation(prompt=args.query)

    elif tag == 'DIR_CREATION':
        utills.dir_creation(prompt=args.query)
        
    elif tag == 'FILE_DELETION':
        utills.file_deletion(prompt=args.query)

    elif tag == 'DIR_DELETION':
        utills.dir_deletion(prompt=args.query)

    elif tag == 'COPY_FILE':
        utills.copy_file(prompt=args.query)

    elif tag == 'INSTALL_PKG':
        utills.install_pkg(prompt=args.query)

    elif tag == 'UNINSTALL_PKG':
        utills.uninstall_pkg(prompt=args.query)

    elif tag == 'SEND_FILE':
        networking.send_file()

    elif tag == 'RECIEVE_FILES':
        networking.receive_file()

    elif tag == 'IP_ADDRESS':
        networking.get_ip()

    elif tag == 'SCAN_NETWORK':
        networking.scan()

    elif tag == 'IS_PKG_INSTALLED':
        networking.check_wrapper(prompt=args.query)

    elif tag == 'CHECK_INTERNET':
        networking.check_internet()

    elif tag == 'PCI_SHOW':
        hardware.list_pci()

    elif tag == 'USB_SHOW':
        hardware.list_usb()

    elif tag == 'SHOW_FILE_CONTENTS':
        utills.cat_file(prompt=args.query)

    elif tag == 'BLOCK_DEVICES':
        hardware.list_blk()

    elif tag == 'LIST_SERVICES':
        utills.list_services()

    elif tag == 'COMPRESS_FILE':
        utills.comporess_file()

    elif tag == 'CHANGE_MAC':
        networking.change_mac_add()
    
    elif tag == 'RESET_MAC':
        networking.reset_mac_add()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-q', '--query', help='Enter the query')

    args = parser.parse_args()
    main(args)
