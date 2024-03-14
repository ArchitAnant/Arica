import subprocess as sb

def list_pci():
    #list the pci devices
    print("Listing PCI devices...")
    sb.run("lspci",shell=True)

def list_usb():
    #list the usb devices
    print("Listing USB devices...")
    sb.run("lsusb",shell=True)

def list_blk():
    #list the block devices
    print("Listing block devices...")
    sb.run("lsblk | grep sd",shell=True)