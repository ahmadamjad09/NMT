import networkx as nx
import matplotlib.pyplot as plt
class Ipgraph:
    def set_Graph(self,ips_list):
        length = len(ips_list)
        G = nx.DiGraph()
        for i in range(length - 1):
            G.add_edge(ips_list[i], ips_list[i + 1])
        nx.draw(G, with_labels=True)
        plt.show()


