from TraceRoute import Traceroute
trace = Traceroute()
trace.findIps("facebook.com")
ip_list = trace.getIpList()
print (ip_list)
