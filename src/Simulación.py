from generadores.LCG import LCG
from generadores.MersenneTwister import MT19937
from generadores.XORShift import XORShift
import numpy as np

LAMDA_MAX = 30  # Tasa máxima de llegadas de clientes. 
LAMDA_EXP = 35  # Tasa de atención de clientes (clientes/hora). 

def exponencial(generador_U):
    U = 1 - generador_U.random()
    return -np.log(U)/LAMDA_EXP

def lamda_t(T):
    return 20 + 10 * np.cos((np.pi * T)/12)

def generador_cliente(T, lamda_t, generador_U):
    NT = 0
    eventos_llegadas = []
    U = 1 - generador_U.random()
    t = -np.log(U) / LAMDA_MAX 
    while t <= T:
        V = generador_U.random()
        if V < lamda_t(t) / LAMDA_MAX:
            NT += 1
            eventos_llegadas.append(t)
            t += -np.log(1 - generador_U.random()) / LAMDA_MAX
    return NT, eventos_llegadas


def simulation(T, generador_U):

    NT,llegadas_clientes = generador_cliente(T, lamda_t, generador_U)
    tiempos_atencion = [exponencial(generador_U) for _ in range(NT)]

    return NT, llegadas_clientes, tiempos_atencion


LCG_ = LCG(12345)
NT, llegadas_clientes, tiempos_atencion = simulation(48, LCG_)     
    
print("Cantidad de eventos en 48 horas: ", NT)
for i, tiempo in enumerate(llegadas_clientes):
    print(f"  Evento {i+1}: {tiempo:.4f}")
    
print("\nTiempos de atencion de los clientes:")
for i, tiempo in enumerate(tiempos_atencion):
    print(f"  Cliente {i+1}: {tiempo:.4f}")

