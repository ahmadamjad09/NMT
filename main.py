from TraceRoute import Traceroute
from IPGraph import Ipgraph
trace = Traceroute()
graph = Ipgraph()
trace.findIps("google.com")
ip_list = trace.getIpList()
print (ip_list)
graph.set_Graph(ip_list)







