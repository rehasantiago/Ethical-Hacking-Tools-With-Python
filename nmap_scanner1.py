import nmap

scanner = nmap.PortScanner()

print("welcome,this is a simple nmap automation tool")
print("<------------------------------------------------>")
ip_addr = input("enter an ip address:")
print("the entered ip address is ",ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan u wanna run
                1)SYN ACK scan
                2)UDP scan
                3)Comprehensive scan""")


print("you have selected option ",resp)

if resp=='1':
    print("nmap version: ",scanner.nmap_version())
    scanner.scan(ip_addr,'1-1024','-v -sS') #2nd parameter is the range of ports
    #to display info
    print(scanner.scaninfo())
    print("IP status: ",scanner[ip_addr].state())#gives the state whether the ip is up or down
    #to print the protocols
    print(scanner[ip_addr].all_protocols())
    print("open ports are: ",scanner[ip_addr]['tcp'].keys())
elif resp=='2':
    print("nmap version: ",scanner.nmap_version())
    scanner.scan(ip_addr,'1-1024','-v -sU') #2nd parameter is the range of ports
    #to display info
    print(scanner.scaninfo())
    print("IP status: ",scanner[ip_addr].state())#gives the state whether the ip is up or down
    #to print the protocols
    print(scanner[ip_addr].all_protocols())
    print("open ports are: ",scanner[ip_addr]['udp'].keys())
elif resp=='3':
    print("nmap version: ",scanner.nmap_version())
    scanner.scan(ip_addr,'1-1024','-v -sS -sV -sC -A -O') #2nd parameter is the range of ports
    #to display info
    print(scanner.scaninfo())
    print("IP status: ",scanner[ip_addr].state())#gives the state whether the ip is up or down
    #to print the protocols
    print(scanner[ip_addr].all_protocols())
    print("open ports are: ",scanner[ip_addr]['tcp'].keys())
elif resp>=4:
    print("please enter a vlaid option")


