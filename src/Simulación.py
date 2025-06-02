import matplotlib.pyplot as plt
from generadores.LCG import LCG
from generadores.MersenneTwister import MT19937
from generadores.XORShift import XORShift
import numpy as np
import math
# Parámetros globales del sistema de colas
LAMDA_MAX = 30  # Tasa máxima de llegadas de clientes (clientes por hora)
LAMDA_EXP = 35  # Tasa media del servicio (clientes por hora)

# Generador de tiempos de atención con distribución exponencial


def exponencial(generador_U):
    # Se usa 1 - U para evitar log(0)
    U = 1 - generador_U.random()
    return round(-math.log(U)/LAMDA_EXP ,4) # Transformación inversa de una exponencial


# Función lambda(t): tasa de llegada variable con el tiempo (cosenoidal)
def lamda_t(T):
    # Llega a 30 en su punto máximo y 10 en el mínimo
    return 20 + 10 * math.cos((math.pi * T)/12)


# Generador de llegadas de clientes con Poisson no homogénea usando thinning
def generador_cliente(T, lamda_t, generador_U):
    NT = 0  # Cantidad total de eventos aceptados
    eventos_llegadas = []  # Tiempos de llegada aceptados
    U = 1 - generador_U.random()
    t = -math.log(U) / LAMDA_MAX  # Tiempo de la primera llegada candidata

    while t <= T:
        V = generador_U.random()
        # Se acepta el evento con probabilidad lamda(t)/LAMDA_MAX
        if V < lamda_t(t) / LAMDA_MAX:
            NT += 1
            eventos_llegadas.append(round(t,4))
            # Generar próximo candidato
            t += -math.log(1 - generador_U.random()) / LAMDA_MAX
    return NT, eventos_llegadas  # Devuelve cantidad y lista de tiempos de llegada


# Función principal de simulación de 0 a T horas
def simulation(T, generador_U):
    NT, llegadas_clientes = generador_cliente(T, lamda_t, generador_U)
    tiempos_atencion = [exponencial(generador_U) for _ in range(NT)]
    return NT, llegadas_clientes, tiempos_atencion


# Función que simula el sistema de colas y extrae métricas
def guardar_info(NT,  llegadas_clientes, tiempos_atencion, horas):
    T = 0  # Tiempo actual del sistema
    tiempo_espera = []  # Clientes que esperaron para ser atendidos
    # Tiempo en que el servidor estuvo libre esperando a un nuevo cliente
    espera_servidor = []
    N = len(llegadas_clientes)
    # Se comienza desde el tiempo de llegada del primer cliente
    # T = llegadas_clientes[0]

    distribucion_longitud_cola = []  # Lista de longitud de la cola en cada evento

    for i in range(N):
        if T >=  horas:
            break
        # Calcular cuántos clientes llegaron antes del tiempo T (aún en espera)
        clientes_en_espera = sum(1 for j in range(
            i, N) if llegadas_clientes[j] < T)
        distribucion_longitud_cola.append((round(T,4), clientes_en_espera - 1 if clientes_en_espera > 0 else 0))

        # Si el cliente llegó antes del tiempo actual, tuvo que esperar
        if llegadas_clientes[i] <= T:
            # Guarda cuánto esperó
            tiempo_espera.append((i + 1, round(T - llegadas_clientes[i], 4)))
            # Se actualiza el tiempo del sistema con la atención
            T += tiempos_atencion[i]
        else:
            # Si llegó después del tiempo actual, no esperó: fue atendido al llegar,
            # se guarda cuanto tuvo que esperar el servidor hasta que llegue un nuevo cliente
            espera_servidor.append((round(T,4), round(llegadas_clientes[i] - T, 4)))
            T = llegadas_clientes[i] + \
                tiempos_atencion[i]  # Nuevo tiempo actual

    return distribucion_longitud_cola, tiempo_espera, espera_servidor


# Porcentaje de tiempo que el servidor está ocupado puede calcularse como la suma
# de todos los tiempos de espera en el que el servidor no estuvo atendiendo clientes.
# Ese resultado se lo restamos a 48 y dividimos todo por 48 horas.
def porcentaje_tiempo_ocupado(espera_servidor, horas):
    # Porcentaje de tiempo que el servidor estuvo ocupado
    total_tiempo_no_atendido = sum(tiempo for _, tiempo in espera_servidor)
    return (horas - total_tiempo_no_atendido) / horas


def tiempo_promedio(atencion_clientes, NT):
    # Tiempo promedio de atención por cliente
    if NT == 0:
        return 0
    return sum(atencion_clientes) / NT

def porcentaje_tiempo_ocupado_por_hora(espera_servidor, horas):
    utilizacion_por_hora = []

    for i in range(horas):
        esperas = [ espera for (hora,espera) in espera_servidor if int(hora) == i] #Se puede optimizar
        tiempo_en_uso = 1 - sum(esperas)
        utilizacion_por_hora.append(tiempo_en_uso * 100)

    return utilizacion_por_hora

    

if __name__ == "__main__":
    # Simulación con un generador LCG
    LCG_ = LCG(12345)
    NT, llegadas_clientes, tiempos_atencion = simulation(48, LCG_)
    tiempo_promedio = tiempo_promedio(tiempos_atencion, NT)

    print(llegadas_clientes)
    print(tiempos_atencion)

    # Se ejecuta la función guardar_info
    distribucion_longitud_cola, tiempo_espera, espera_servidor = guardar_info(
        0, llegadas_clientes, tiempos_atencion, 48)
    porcentaje = porcentaje_tiempo_ocupado(espera_servidor, 48)*100

    ## Impresión de resultados
    print("\nDistribución de la longitud de la cola:")
    print(distribucion_longitud_cola)

    #print("\nTiempos de espera de los clientes:")
    #for cliente, tiempo in tiempo_espera:
    #    print(f"  Cliente {cliente}: {tiempo:.2f}")
    #
    #print("\nTiempos no atendidos de los clientes:")
    #for cliente, tiempo in espera_servidor:
    #    print(f"  Cliente {cliente}: {tiempo:.2f}")

    print(
        f"\nPorcentaje de tiempo que el servidor estuvo ocupado: {porcentaje:.2f}%")
    print(f"Tiempo promedio de atención por cliente: {tiempo_promedio:.2f} horas")