import matplotlib.pyplot as plt
import numpy as np
from generadores.LCG import LCG
from generadores.XORShift import XORShift
from generadores.MersenneTwister import MT19937

N = 10002


def plot_histograma(datos, titulo, nombre_archivo):
    plt.hist(datos, bins=50, range=(0, 1), edgecolor='black', alpha=0.7)
    plt.title(titulo)
    plt.xlabel("Valor generado")
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.savefig(nombre_archivo)
    plt.close()


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


def plot_cubo(datos, titulo, nombre_archivo):
    xs = datos[0::3]
    ys = datos[1::3]
    zs = datos[2::3]

    fig = plt.figure()
    plt.title(titulo)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs, ys, zs, c='r', marker='o')
    ax.set_xlabel('X_i')
    ax.set_ylabel('X_{i+1}')
    ax.set_zlabel("X_{i+2}")

    # Rotar el cubo 
    ax.view_init(elev=70, azim=55)

    plt.savefig(nombre_archivo)
    plt.close()


if __name__ == "__main__":
    generadores = [
        ("LCG", LCG(12345)),
        ("XORShift", XORShift(12345)),
        ("MersenneTwister", MT19937(12345))
    ]

    for nombre, generador in generadores:
        datos = [generador.random() for _ in range(N)]
        plot_histograma(
            datos, f"Histograma-{nombre}", f"results/graficos/generadores/Histograma_{nombre}.png")
        plot_pares(datos, f"Pares-{nombre}",
                   f"results/graficos/generadores/Pares_{nombre}.png")
        plot_cubo(datos, f"Cubo-{nombre}",
                  f"results/graficos/generadores/Cubo_{nombre}.png")
