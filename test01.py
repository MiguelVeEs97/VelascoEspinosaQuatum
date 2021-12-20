import networkx as nx
import dwave_networkx as dnx
import matplotlib.pyplot as plt


#Introducimos librerias Ocean
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

#Definimos el grafo de 6 nodos
s5 = nx.star_graph(5)
G=nx.Graph()
G.add_nodes_from(["1","2","3","4","5","6"])
G.add_edge("1","2")
G.add_edge("1","3")
G.add_edge("2","3")
G.add_edge("2","4")
G.add_edge("3","4")
G.add_edge("3","5")
G.add_edge("4","5")
G.add_edge("2","6")
G.add_edge("4","6")

#Lo dibujamos
nx.draw(G, with_labels = True)
plt.savefig("networkx6.png")




