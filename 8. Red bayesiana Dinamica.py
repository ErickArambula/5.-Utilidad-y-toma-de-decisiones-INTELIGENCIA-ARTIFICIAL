from pgmpy.models import DynamicBayesianNetwork as DBN
from pgmpy.factors.discrete import TabularCPD

# Creación de la estructura de la DBN
dbn = DBN()

# Definición de variables y CPDs (Conditional Probability Distributions)
estado_t = TabularCPD(variable='Estado_t', variable_card=2, values=[[0.7], [0.3]])
estado_t1 = TabularCPD(variable='Estado_t1', variable_card=2, values=[[0.9, 0.6], [0.1, 0.4]],
                      evidence=['Estado_t'], evidence_card=[2])

# Agregar variables y CPDs a la DBN
dbn.add_node(estado_t)
dbn.add_edge(estado_t, estado_t1)
dbn.add_cpds(estado_t, estado_t1)

# Finalizar la estructura de la DBN
dbn.finalize()

# Verificar si la DBN es válida
valida = dbn.check_model()
print("¿La DBN es válida?", valida)

# Consulta de probabilidades condicionales
from pgmpy.inference import DBNInference
inference = DBNInference(dbn)
resultados = inference.query(variables=['Estado_t1'], evidence={'Estado_t': 1})
print(resultados)
