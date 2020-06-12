import os
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
