import subprocess as sb
import time

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
