#BIBLIOTECAS
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import networkx as nx
import dwave_networkx as dnx
import matplotlib.pyplot as plt

#Obtener el sampler
sampler = EmbeddingComposite(DWaveSampler())

#Crear un grafo de 6 puntas y juntarlos todos
G=nx.Graph()
G.add_nodes_from(['1','2','3','4','5','6'])
G.add_edge('1','2')
G.add_edge('1','3')
G.add_edge('3','2')
G.add_edge('3','4')
G.add_edge('3','5')
G.add_edge('2','4')
G.add_edge('2','6')
G.add_edge('5','4')
G.add_edge('4','6')

#Dibujar y almacenar
nx.draw(G, with_labels = True)
plt.savefig('grafo6mio.png')

#Resolver el problema
print(dnx.min_vertex_cover(G,sampler))


