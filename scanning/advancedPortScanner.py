from socket import *
import optparse #for the help options
from threading import *

def conScan(tgtHost,tgtPort):
    try:
        sock = socket(AF_INET,SOCK_STREAM)
        sock.connect((tgtHost,tgtPort))
        print('%d open' % tgtPort)
    except:
        print('%d closed' % tgtPort)
    finally:
        sock.close()

def portScan(tgtHost,tgtPorts):
    try:
        tgtIP = gethostname(tgtHost) #if the user enters hostname instead of ip adress
    except:
        print('Unknown adress')
    try:
        tgtName = gethostbyaddr(tgtIP)#returns a tuple containing hostname,alias list for the IP address,ip adress
        print('scanning for the name of the host is %s' %tgtName)
    except:
        print('scanning for %s' % tgtHost)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target = conScan,args = (tgtHost,int(tgtPort)))#name  of the function to be called and next is the args that need to be passed to the function
        t.start()



def main():
    parser = optparse.OptionParser('usage of program '+'-H <target host> -p <target ports>')
    parser.add_option('-H',dest='tgtHost',type='string',help='specify the target host')#to add an option,dest is the location where the value will be stores and it is of type string
    parser.add_option('-p',dest='tgtPorts',type='string',help='specify the target ports')
    (options,args) = parser.parse_args()#options is a dictionary with tgtHost and tgtPorts
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPorts).split(',')
    if(tgtHost==None) | (tgtPorts[0]==None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost,tgtPorts)


if __name__ == 'main':
    main()
main()
