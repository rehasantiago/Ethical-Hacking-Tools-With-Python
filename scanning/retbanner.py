import socket

def retbanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        sock = socket.socket()
        sock.connect((ip,port))
        banner = sock.recv(1024)
        return banner
    except:
        return



def main():
    ip = input("enter the ip address:")
    for port in range(1,100):
        banner = retbanner(ip,port)
        if banner:
            print("ip:"+ip+" port:"+str(port)+" banner:"+banner)


main()
