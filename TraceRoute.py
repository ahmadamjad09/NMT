import os
import re
class Traceroute:
    def __init__(self):
        self.__command = "traceroute "
        self.__ip_list = []
    def findIps(self,ip):
        self.__command = self.__command + ip
        stream = os.popen(self.__command)
        for line in stream:
         start_index = line.find('(')
         end_index = line.find(')')
         if start_index == -1:
            continue
         ip = line[start_index + 1:end_index]
         self.__ip_list.append(ip)
    def getIpList(self):
        return self.__ip_list
    def getIp_Network(self,ip):
     command = "nmap -sn "
     command = command + ip
     stream = os.popen(command)
     #print (stream.read())
     string = []
     for line in stream:
         if line[0] == 'N':
           ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
           print (ip)
           string.append(ip)
     #result = stream.read()
     print (string)
     return string




