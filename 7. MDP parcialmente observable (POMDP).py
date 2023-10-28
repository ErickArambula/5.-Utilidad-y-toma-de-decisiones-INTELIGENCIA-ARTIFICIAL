from pomdp_py.framework import Agent, Model, Policy, POMDPModel, Belief, update_belief
from pomdp_py.utils import compute_J, print_policy
import random

# Definición de estados, acciones y observaciones
estados = [1, 2, 3, 4, 5]  # Estados: Representan ubicaciones en el laberinto
acciones = [0, 1, 2, 3]  # Acciones: 0 - Mover hacia arriba, 1 - Mover hacia abajo, 2 - Mover hacia la izquierda, 3 - Mover hacia la derecha
observaciones = [0, 1]  # Observaciones: 0 - No ve el tesoro, 1 - Ve el tesoro

# Modelo POMDP
class TesoroModel(Model):
    def sample(self, estado, accion):
        transiciones = [1.0, 0.0, 0.0, 0.0, 0.0]  # Supongamos una probabilidad determinista de movimiento
        return random.choices(estados, weights=transiciones)[0]

    def sample_observation(self, estado, accion, proximo_estado):
        if proximo_estado == 5:  # Si el próximo estado es el tesoro
            return random.choices(observaciones, weights=[0.2, 0.8])[0]  # Probabilidad de ver el tesoro
        else:
            return random.choices(observaciones, weights=[0.8, 0.2])[0]  # Probabilidad de no ver el tesoro

# Definición del modelo POMDP
modelo_pomdp = POMDPModel(estados, acciones, observaciones, TesoroModel())

# Agente
class TesoroAgent(Agent):
    def __init__(self):
        self.policy = None

    def act(self, estado, observacion):
        return self.policy(estado, observacion)

# Creación del agente
agente = TesoroAgent()

# Creación de una política (política aleatoria)
policy = Policy(estados, observaciones, acciones)
for estado in estados:
    for observacion in observaciones:
        for accion in acciones:
            policy.set_distribution(accion, estado, observacion, 1.0 / len(acciones))
agente.policy = policy

# Creación de la creencia inicial
beliefs = [0.2, 0.2, 0.2, 0.2, 0.2]  # Supongamos una creencia uniforme inicial
creencia = Belief(estados, beliefs)

# Actualización de la creencia después de tomar una acción y recibir una observación
accion = agente.act(3, 0)  # Supongamos que estamos en el estado 3 y no vemos el tesoro
proximo_estado = modelo_pomdp.sample(3, accion)
observacion = modelo_pomdp.sample_observation(proximo_estado, accion, proximo_estado)
creencia = update_belief(modelo_pomdp, creencia, accion, observacion)

# Mostrar la política del agente
print_policy(agente.policy)
