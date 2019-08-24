from socket import *
import optparse #for the help options
from threading import *

def main():
    parser = optparse.OptionParser('usage of program '+'-H <target host> -p <target ports>')
    parser.add_option('-H',dest='tgtHost',type='string',help='specify the target host')
    parser.add_option('-p',dest='tgtPorts',type='string',help='specify the target ports')
    (options,args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPorts).split(',')
    if(tgtHost==None) | (tgtPorts[0]==None):
        print(parser.usage)
        exit(0)

main()
