import subprocess as sb

#send data over netcat
def send_file():
    print("Sending file...")
    file_name = input("Enter the file name: ")
    port_no = input("Enter the port number: ")
    ip = input("Enter the IP address: ")
    #check if port is empty
    if port_no == "":
        port_no = "9999"
    #send file over netcat
    sb.run("netcat -w 1 {} {} < {}".format(ip,int(port_no),file_name),shell=True)
    print("File sent successfully")

#receive data over netcat
def receive_file():
    print("Receiving file...")
    file_name = input("Enter the file name: ")
    port_no = input("Enter the port number: ")
    #check if port is empty
    if port_no == "":
        port_no = "9999"
    #receive file over netcat
    sb.run("netcat -lnvp {} > {}".format(port_no,file_name),shell=True)
    print("File received successfully")
    # close the netcat connection

def get_adp():
    adp = sb.run('ip link show | grep "state UP"',shell=True,capture_output=True).stdout.decode("utf-8").split(": ")
    return adp[1]

def get_ip():
    #get the ip address of the system
    ip_r = sb.run('ifconfig {} | grep "inet "'.format(get_adp()),shell=True,capture_output=True).stdout.decode("utf-8").split("netmask")[0]
    ip = ip_r.split("inet ")[1]
    print("IP address : ",ip)
    return ip

def check_wrapper(prompt):
    #check if a package is installed
    package_r = prompt.split("package")[1]
    package = package_r.split("installed")[0].strip()
    if check(package):
        print("{} is installed".format(package))
    else:
        print("{} is not installed".format(package))


def check(package):
    #hidden check for arp-scan
    out = sb.run("{} --help".format(package),shell = True, stdout=sb.PIPE, stderr=sb.STDOUT).returncode
    if out == 0:
        return True
    else:
        return False

def scan():
    if check("arp-scan"):
        print("Scanning the network for devices...")
        sb.run("sudo arp-scan -l",shell=True)
        print("Scanning complete..")
    else:
        print("Scanning the network for devices...")
        sb.run("arp -a",shell=True)
        print("Scanning complete...")


def check_internet():
    #check if internet is available
    code = sb.run("ping -w 2 google.com",shell=True).returncode
    if code == 0:
        print("Internet is available...")
    else:
        print("Internet is not available...")
