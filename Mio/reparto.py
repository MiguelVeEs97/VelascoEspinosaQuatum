#Bibliotecas
import dwavebinarycsp
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

#Samplers a utilizar
sampler = EmbeddingComposite(DWaveSampler())

#Función de ligaduras o constraints
##############################################################
##  mercancia     -->       1: Congelado               0: No congelado
##  cliente  -->            1: Prioritario             0: No prioritario
##  Tiempo trayecto    -->  1: Menos de dos horas      0: Mas de dos horas
##  Distancia trayecto  --> 1: menos o igual a 200 km  0: mas de 200 km
##  Transporte empleado --> 1: Camioneta               0: Cualquier otro
##############################################################

def organizacion(mercancia, cliente, tiempo, km, transporte):
    if mercancia:
        return(tiempo and km and transporte)
    elif cliente:
        return(tiempo and transporte)
    else:
        return(km and not transporte)

#Creamos el problema binario
csp=dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
csp.add_constraint(organizacion,['mercancia', 'cliente', 'tiempo', 'km', 'transporte'])

#Generamos ahora la función energía
bqm=dwavebinarycsp.stitch(csp)

#Sampleamos ahora 6000 puntos y buscamos los mínimos absolutos
response = sampler.sample(bqm, num_reads=6000)

#Mostramos donde están los mínimos absolutos y cuantas veces se han obtenido
#dichos puntos
print(response)

#Lo mostramos de una manera legible
total = 0
for sample, energy, occurences in response.data(['sample', 'energy', 'num_occurrences']):
    total = occurences+total
    mercancia = 'Congelado' if sample['mercancia'] else 'No congelado'
    cliente = 'prioritario' if sample['cliente'] else 'no prioritario'
    tiempo = 'corto' if sample['tiempo'] else 'largo'
    km = 'menor de 200 km' if sample['km'] else 'mayor de 200 km'
    transporte = 'una camioneta' if sample['transporte'] else 'otro transporte distinto a la camioneta'

    print('''
    {}: La mercancía {} a un cliente {} debe de entregarse en un tiempo {} 
    siendo el trayecto {} y el transporte empleado es {}
    '''.format(occurences,mercancia,cliente,tiempo,km,transporte))

            

