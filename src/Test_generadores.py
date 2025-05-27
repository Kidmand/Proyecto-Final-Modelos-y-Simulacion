
import pytest
import numpy as np
import math 
from generadores.LCG import LCG
from generadores.MersenneTwister import MT19937
from generadores.XORShift import XORShift

#==========================TEST REPETIBILIDAD==========================

def test_repetibilidad():
    # Creamos una lista de 5 uniformes y vemos si ambos objetos con la misma semilla producen los mismo valores uniformes.  
    LCG_1 = LCG(12345)
    LCG_2 = LCG(12345)
    XOR_1 = XORShift(12345)
    XOR_2 = XORShift(12345)
    MT_1 = MT19937(12345)
    MT_2 = MT19937(12345)

    assert [LCG_1.random() for _ in range(5)] == [LCG_2.random() for _ in range(5)]
    assert [XOR_1.random() for _ in range(5)] == [XOR_2.random() for _ in range(5)]
    assert [MT_1.random() for _ in range(5)] == [MT_2.random() for _ in range(5)]

 
#==========================TEST UNIFORMIDAD==========================

EXPECTED_MEAN = 0.5
EXPECTED_VARIANCE = 1/12
MEAN_TOLERANCE = 0.005  # La media debe estar muy cerca de 0.5
VARIANCE_TOLERANCE = 0.002 # La varianza debe estar muy cerca de 0.083333
N_SAMPLES = 100000

def test_uniformidad():
    #Verifica la uniformidad del LCG, XORShift y MersenneTwister calculando la media y varianza
    #de una gran cantidad de números generados.

    # LCG
    LCG_ = LCG(seed=12345)
    numbers_LCG = [LCG_.random() for _ in range(N_SAMPLES)]

    actual_mean_LCG = np.mean(numbers_LCG)
    actual_variance_LCG = np.var(numbers_LCG)

    # XORShift
    XOR_ = XORShift(seed=12345)
    numbers_XOR = [XOR_.random() for _ in range(N_SAMPLES)]

    actual_mean_XOR = np.mean(numbers_XOR)
    actual_variance_XOR = np.var(numbers_XOR)

    # MT
    MT_ = MT19937(seed=12345)
    numbers_MT = [MT_.random() for _ in range(N_SAMPLES)]

    actual_mean_MT = np.mean(numbers_MT)
    actual_variance_MT = np.var(numbers_MT)

    # Assert LCG
    assert actual_mean_LCG == pytest.approx(EXPECTED_MEAN, abs=MEAN_TOLERANCE)
    assert actual_variance_LCG == pytest.approx(EXPECTED_VARIANCE, abs=VARIANCE_TOLERANCE)
    # Assert XORShift
    assert actual_mean_XOR == pytest.approx(EXPECTED_MEAN, abs=MEAN_TOLERANCE)
    assert actual_variance_XOR == pytest.approx(EXPECTED_VARIANCE, abs=VARIANCE_TOLERANCE)
    # Assert MT
    assert actual_mean_MT == pytest.approx(EXPECTED_MEAN, abs=MEAN_TOLERANCE)
    assert actual_variance_MT == pytest.approx(EXPECTED_VARIANCE, abs=VARIANCE_TOLERANCE)


#==========================TEST CORRELACIÓN==========================

def test_correlation():
        # LCG
    LCG_ = LCG(seed=12345)
    numbers_LCG = [LCG_.random() for _ in range(N_SAMPLES)]

    actual_mean_LCG = np.mean(numbers_LCG)
    actual_variance_LCG = np.var(numbers_LCG)

    # XORShift
    XOR_ = XORShift(seed=12345)
    numbers_XOR = [XOR_.random() for _ in range(N_SAMPLES)]

    actual_mean_XOR = np.mean(numbers_XOR)
    actual_variance_XOR = np.var(numbers_XOR)
    actaul_correlation = 

    # MT
    MT_ = MT19937(seed=12345)
    numbers_MT = [MT_.random() for _ in range(N_SAMPLES)]

