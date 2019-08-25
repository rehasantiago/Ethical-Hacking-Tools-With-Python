import socket
import os
import sys

def retBanner(ip,port):
    try:
        socket.defaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVul(banner,filename):
    f = open(filename,'r')
    for line in f.readlines():
        if line.strip("\n") in banner:
            print(banner" is vulnerable")

def main():
    if len(sys.argv)==2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):#to check if file exists in the path or not
            print("file does not exit")
            exit(0)
        if not os.access(filename,os.R_OK):
            print("file is not accessible")
            exit(0)
    else:
        print("Usage "+sys.argv[0]+" <vul filename>")
        exit(0)
    portlist = [21,22,25,80,110,443,445]
    for x in range(4,6):
        ip = "192.168.1."+str(x)
        for port in portlist:
            banner = retBanner(ip,port)
            if banner:
                print("ip:"+ip+" port:"+str(port)+" banner:"+banner)
                checkVul(banner,filename)

main()