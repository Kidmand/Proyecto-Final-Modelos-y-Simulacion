from Simulación import guardar_info, porcentaje_tiempo_ocupado
import pytest 

def test_guardar_info_simple():

    # Ejemplo de uso (comentado en el código original)
    horas = 4
    # Porcentaje de uso del servidor en 4 horas = 75%
    llegadas_clientes = [1, 2, 2.1, 2.2, 2.25, 2.256, 2.35, 2.7, 3.08]
    tiempos_atencion =  [1, 1, 0.5, 0.2, 0.1, 0.2, 0.3, 0.21, 0.30 ]


    distribucion_longitud_cola, tiempo_espera, espera_servidor = guardar_info(
        0, llegadas_clientes, tiempos_atencion, horas)
    porcentaje = porcentaje_tiempo_ocupado(espera_servidor, horas)*100

    assert porcentaje == 75.0
    assert distribucion_longitud_cola == [(0, 0), (2, 0), (3, 5), (3.5, 5), (3.7, 4), (3.8, 3)]
    assert tiempo_espera == [(2,0),(3,0.9), (4,1.3), (5,1.45), (6,1.544)]
    assert espera_servidor == [(0, 1)]

def test_guardar_info_extenso():
    llegadas_clientes = [0.0034, 0.1017, 0.1021, 0.1505, 0.2323, 0.2459, 0.2562, 0.3938, 0.4076, 0.4179, 0.4845, 0.5674, 0.6561, 0.6683, 0.6922, 0.7728, 0.9071, 0.9961]
    tiempos_atencion =  [0.0624, 0.0126, 0.0032, 0.0339, 0.025, 0.0079, 0.0056, 0.1642, 0.0105, 0.0216, 0.0353, 0.0265, 0.0197, 0.0136, 0.0261, 0.0112, 0.0369, 0.0039]
    horas = 1

    distribucion_longitud_cola, tiempo_espera, espera_servidor = guardar_info(
        0, llegadas_clientes, tiempos_atencion, horas)
    porcentaje = porcentaje_tiempo_ocupado(espera_servidor, horas)*100

    assert porcentaje == 52.01
    assert distribucion_longitud_cola == [(0, 0), (0.0658, 0), (0.1143, 0), (0.1175, 0), (0.1844, 0), (0.2573, 1), (0.2652, 0), (0.2708, 0), (0.558, 2), (0.5685, 2), (0.5901, 1), (0.6254, 0), (0.6519, 0), (0.6758, 0), (0.6894, 0), (0.7183, 0), (0.784, 0), (0.944, 0)]
    assert tiempo_espera == [(3,0.0122),(6,0.0114), (7,0.009), (9, 0.1504), (10, 0.1506), (11, 0.1056), (12, 0.058), (14, 0.0075)]
    assert espera_servidor == [(0, 0.0034), (0.0658, 0.0359), (0.1175, 0.033), (0.1844, 0.0479), (0.2708, 0.123), (0.6519, 0.0042), (0.6894, 0.0028), (0.7183, 0.0545), (0.784, 0.1231), (0.944, 0.0521)]