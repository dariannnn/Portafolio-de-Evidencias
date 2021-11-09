import socket
import sys

def validIP(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True

ipList = []
portlist = [139,22,23,25,80]

for eachLine in sys.stdin:
    entry = eachLine.strip()
    if entry:
        ipList.append(entry)
        
for ip in ipList:
    if validIP(ip):
        print(ip)
        for port in portlist:
            sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result=sock.connect_ex((ip,port))
            if result == 0:
                print(f"Puerto {port}: \t Abierto")
            else:
                print(f"Puerto {port}: \t Cerrado")
            sock.close()
        print("\n")
        
        
