import nmap

ip_addr = input("enter the ip adress:")
port = input("enter the port:")

nm_scan = nmap.PortScanner()
print("\nRunning....\n")
nm_scanner = nm_scan.scan(ip_addr,port,arguments = '-O')
#print nm_scanner to understand the below steps
host_is_up = "the host is: "+nm_scanner['scan'][ip_addr]['status']['state']+'.\n'
port_open = "the port "+port+" is "+nm_scanner['scan'][ip_addr]['tcp'][int(port)]['state']+'.\n'
method_scan = "the method of scanning is "+nm_scanner['scan'][ip_addr]['tcp'][int(port)]['reason']+'.\n'
guessed_os = "there is %s chance that the host is running %s"%(nm_scanner['scan'][ip_addr]['osmatch'][0]['accuracy'],nm_scanner['scan'][ip_addr]['osmatch'][0]['name'])
print(host_is_up)
print(port_open)
print(method_scan)
print(guessed_os)
