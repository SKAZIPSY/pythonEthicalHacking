# this tool is same like a nmap to scan port hosting sites
import socket

targets = input("[*] Enter target to scan (split them with ,)")
ports = int(input("[*] Enter how many ports you want to scan "))


def scan_port(ipaddress, port):
    try:
        #  socket/post ae those that host a website
        sock = socket.socket()
        # sock to conect needs two parameter
        sock.connect((ipaddress, port))
        # if we manage to connect then the port is open  and if we dont then the port is closed
        print("[+] Port Open " + str(port))
        socket.close()
    except:
        print("[-] Port Close " + str(port))


def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)


if ',' in targets:
    # if multiple targets are to scan
    for ipadd in targets.split(','):
        scan(ipadd.strip(' '), ports)
else:
    scan(targets, ports)
