from generadores.LCG import LCG
from generadores.MersenneTwister import MT19937
from generadores.XORShift import XORShift
import numpy as np

def lamda_t(T):
    return 20 + 10 * np.cos((np.pi * T)/12)

def generador_cliente(T, lamda_t, generador_U):
    NT = 0
    eventos_llegadas = []
    U = 1 - generador_U()
    t = -log(U) / lamda 
    while t <= T:
        V = generador_U()
        if V < lamda_t(t) / lamda:
        NT += 1
        eventos_llegadas.append(t)
        t += -log(1 - generador_U()) / lamda
    return NT, eventos_llegadas


def simulation(T, generador_U):

    NT,llegadas_clientes = generador_cliente(T, lamda_t, generador_U)
    tiempos_atencion = [np.exp(1/35, 48) for _ in range(NT)]
    
    #COMPLETAR