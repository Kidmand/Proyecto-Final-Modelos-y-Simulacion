import time
from generadores import MersenneTwister
from generadores.LCG import LCG
from generadores.MersenneTwister import MT19937
from generadores.XORShift import XORShift


def medir_tiempo(gen, nombre):
    repeticiones = 1_000_000

    inicio = time.time()
    [gen.random() for _ in range(repeticiones)]
    fin = time.time()

    print(f"{nombre} tarda {fin - inicio:.4f} segundos en generar {repeticiones} números")


if __name__ == "__main__":
    gen_lcg = LCG(12345)
    gen_mt = MT19937(12345)
    gen_xor = XORShift(12345)

    medir_tiempo(gen_lcg, "LCG")
    medir_tiempo(gen_mt, "MersenneTwister")
    medir_tiempo(gen_xor, "XORShift")
