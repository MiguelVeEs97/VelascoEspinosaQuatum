#BIBLIOTECAS
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import networkx as nx
import dwave_networkx as dnx
import matplotlib.pyplot as mpl

#Ajustar el problema a DWave (Embedding) y obtener el sampler seleccionado
#El sampler posteriormente ejecutará el problema, lo dejará correr y encontrará los mínimos al problema
#Se lanzará un número de veces que se quiera, en este caso solamente una vez
sampler = EmbeddingComposite(DWaveSampler())

#Generar la estrella de 5 puntas
s5 = nx.star_graph(5)

#Plantear el problema (Con el menor número de nodos, que se toquen todas las aristas)
#Resolver el problema, diciendo que lo resuelva con el sampler escrito
print(dnx.min_vertex_cover(s5,sampler))

#Dibujar la estrella
nx.draw(s5, with_labels = True)

#Guardar la estrella y representarla
mpl.savefig("grafico5mio.png")

