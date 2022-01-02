#Bibliotecas
import dwavebinarycsp
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

#Obtener el sampler
sampler=EmbeddingComposite(DWaveSampler())

#Crear la función ligadura o constraint
def planifica(horario, ubicacion, duracion, asistencia):
    if horario:
        return (ubicacion and asistencia)
    else:
        return (not ubicacion and not duracion)

#Relacionar las variables (y decir que son binarias) con las ligaduras
csp=dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
csp.add_constraint(planifica,['horario','ubicacion','duracion','asistencia'])

#Generar la función de energía
bqm=dwavebinarycsp.stitch(csp)

#Samplear 5000 puntos y encontrar los mínimos absolutos
response=sampler.sample(bqm,num_reads=5000)
print(response)




