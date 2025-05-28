import matplotlib.pyplot as plt
import numpy as np
from generadores.LCG import LCG
from generadores.XORShift import XORShift
from generadores.MersenneTwister import MT19937

N = 100000

def plot_histograma(datos, titulo, nombre_archivo):
    plt.hist(datos, bins=50, range=(0, 1), edgecolor='black', alpha=0.7)
    plt.title(titulo)
    plt.xlabel("Valor generado")
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.savefig(nombre_archivo)
    plt.close()
    
def generar_histogramas():
    generadores = [
        ("LCG", LCG(12345)),
        ("XORShift", XORShift(12345)),
        ("MersenneTwister", MT19937(12345))
    ]
    
    for nombre, generador in generadores:
        datos = [generador.random() for _ in range(N)]
        plot_histograma(datos,f"Histograma-{nombre}", f"results/Graficos/Histograma_{nombre}.png")
    
def plot_pares(datos, titulo, nombre_archivo):
    x = datos[:-1]
    y = datos[1:]
    
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, s=1)
    plt.title(titulo)
    plt.xlabel("X_i")
    plt.ylabel("X_{i+1}")
    plt.grid(True)
    plt.savefig(nombre_archivo)
    plt.close()

def generar_grafico_pares():
    generadores = [
        ("LCG", LCG(12345)),
        ("XORShift", XORShift(12345)),
        ("MersenneTwister", MT19937(12345))
    ]
    
    for nombre, generador in generadores:
        datos = [generador.random() for _ in range(N)]
        plot_pares(datos,f"Pares-{nombre}", f"results/Graficos/Pares_{nombre}.png")

    
        
if __name__ == "__main__":
    generar_histogramas()
    generar_grafico_pares()