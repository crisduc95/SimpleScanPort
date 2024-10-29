import socket
from colorama import Fore

class ScanHost:

    def __init__(self, ip="127.0.0.1", portI=1, portF=1024, timeout=1):
        self.ip = ip
        self.portI = portI
        self.portF = portF
        self.timeout = timeout
    
    def __scanTcp(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    
    def singleScan(self):
        if self.__scanTcp(self.ip, self.portI):
            print(f"{Fore.LIGHTGREEN_EX}{self.ip} : {self.portI} is OPEN")
        else:
            print(f"{Fore.LIGHTRED_EX}{self.ip} : {self.portI} is CLOSE")
    
    def muestra(self):
        for port in range (self.portI, (self.portF + 1)):
            if self.__scanTcp(self.ip, port):
                print(f"{Fore.LIGHTGREEN_EX}{self.ip} : {port} is OPEN")
            else:
                print(f"{Fore.LIGHTRED_EX}{self.ip} : {port} is CLOSE")

