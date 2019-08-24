import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#last parameter stands for tcp packet
socket.setdefaulttimeout(2)#after 2 secs it'll stop 


host = input("Enter the host to scan: ")
#port = int(input("Enter the port to scan: "))


for port in range(1,100):
    if(sock.connect_ex((host,port))):
        print (colored("%d port is closed" % (port),'red'))
    else:
        print (colored("%d port is open" % (port),'green'))
