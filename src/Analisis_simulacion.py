import matplotlib.pyplot as plt
import numpy as np

from generadores.LCG import LCG
from generadores.XORShift import XORShift
from generadores.MersenneTwister import MT19937

from Simulación import guardar_info, porcentaje_tiempo_ocupado, simulation, porcentaje_tiempo_ocupado_por_hora

HORAS = 48

def evolucion_longitud_de_cola(distribucion_longitud_cola, titulo, nombre_archivo):
    tiempos = [t for t, l in distribucion_longitud_cola]
    longitudes = [l for t, l in distribucion_longitud_cola]

    plt.figure(figsize=(10, 5))
    plt.step(tiempos, longitudes, where='post', color='blue')
    plt.xlabel("Tiempo (horas)")
    plt.ylabel("Longitud de la cola")
    plt.title(titulo)
    plt.grid(True)
    plt.savefig(nombre_archivo)
    plt.close()

def histograma_tiempos_de_espera(tiempo_espera, titulo, nombre_archivo):
    esperas = [e for _, e in tiempo_espera]
    n = len(tiempo_espera)
    #Usamos regla de Sturges
    num_bins = int(np.ceil(np.log2(n)+1))

    plt.hist(esperas, bins=num_bins, edgecolor='black', color='pink')
    plt.xlabel("Tiempo de espera (horas)")
    plt.ylabel("Cantidad de clientes")
    plt.title(titulo)
    plt.grid(True)
    plt.savefig(nombre_archivo)
    plt.close()

def utilizacion_servidor(utilizacion_horas, titulo, nombre_archivo):
    horas = list(range(len(utilizacion_horas)))  # 0 a 47

    plt.plot(horas, utilizacion_horas, linestyle='-')
    plt.title(titulo)
    plt.xlabel('Hora')
    plt.ylabel('Utilización (%)')
    plt.grid(True)
    plt.xticks(horas[::2])
    plt.savefig(nombre_archivo)
    plt.close()

def tiempo_entre_arribos(llegadas_clientes, titulo, nombre_archivo):
    entre_arribos = [llegadas_clientes[i+1] - llegadas_clientes[i] for i in range(len(llegadas_clientes)-1)]
    n = len(entre_arribos)
    #Usamos regla de Sturges
    num_bins = int(np.ceil(np.log2(n)+1))

    plt.hist(entre_arribos, bins=num_bins, edgecolor='black', color='pink')
    plt.xlabel("Tiempo entre arribos (horas)")
    plt.ylabel("Frecuencia")
    plt.title(titulo)
    plt.grid(True)
    plt.savefig(nombre_archivo)
    plt.close()

def tiempo_entre_servicios( NT, espera_servidor , titulo, nombre_archivo):
    faltan_ceros = NT - len(espera_servidor) 
    entre_servicios = [inactividad for _,inactividad in espera_servidor] + [0]*faltan_ceros

    n = len(entre_servicios)
    #Usamos regla de Sturges
    num_bins = int(np.ceil(np.log2(n)+1))

    plt.hist(entre_servicios, bins=num_bins, edgecolor='black', color='pink')
    plt.xlabel("Tiempo entre servicios (horas)")
    plt.ylabel("Frecuencia")
    plt.title(titulo)
    plt.grid(True)
    plt.savefig(nombre_archivo)
    plt.close()


if __name__ == "__main__":
    generadores = [
        ("LCG", LCG(12345)),
        ("XORShift", XORShift(12345)),
        ("MersenneTwister", MT19937(12345))
    ]

    for nombre, generador in generadores:
        NT, llegadas_clientes, tiempos_atencion = simulation(HORAS, generador)
        distribucion_longitud_cola, tiempo_espera, espera_servidor = guardar_info(
            0, llegadas_clientes, tiempos_atencion, HORAS)
        utilizacion_horas = porcentaje_tiempo_ocupado_por_hora(espera_servidor, HORAS)
        evolucion_longitud_de_cola(
            distribucion_longitud_cola, f"Longitud Cola {nombre}", f"results/Longitud_{nombre}.png")
        histograma_tiempos_de_espera(
            tiempo_espera, f"Histograma Espera {nombre}", f"results/Espera_{nombre}.png")
        utilizacion_servidor(
            utilizacion_horas, f"Evolucion del uso por hora {nombre}", f"results/Uso_{nombre}.png")
        tiempo_entre_arribos(
            llegadas_clientes, f"Tiempo entre arribos-{nombre}", f"results/Arribos_{nombre}.png")
        tiempo_entre_servicios( 
            NT, espera_servidor , f"Tiempo entre servicios-{nombre}", f"results/Servicios_{nombre}.png")