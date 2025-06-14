#!/bin/bash

export PYTHONPATH=src

while true; do

    echo ""
    echo "=== Proyecto Modelos y Simulación ==="
    echo ""
    echo "¿Qué querés hacer?"
    echo "1 - Ejecutar tests (pytest)"
    echo "2 - Ejecutar análisis de generadores"
    echo "3 - Ejecutar análisis de simulación"
    echo "0 - Salir"
    echo ""
    read -p "Elegí una opción (0-3): " opcion

    case $opcion in
        1) 
            echo ">> Ejecutando tests con pytest..."
            pytest src/test
            echo ""
            read -p "Presioná Enter para continuar..."
            ;;
        2)  
            echo ">> Ejecutando análisis de generadores..."
            echo ">> Generando gráficos de análisis"
            python3 src/analisis/Analisis_generadores.py
            echo ">> Gráficos guardados en results/graficos/generadores"
            echo ">> Iniciando prueba de velocidad..."
            python3 src/analisis/Medir_tiempos.py
            echo ""
            read -p "Presioná Enter para continuar..."
            ;;
        3) 
            echo ">> Ejecutando análisis de simulación..."
            echo ">> Generando gráficos de análisis de la simulación"
            python3 src/analisis/Analisis_simulacion.py
            echo ">> Gráficos guardados en results/graficos/simulacion"
            echo ""
            read -p "Presioná Enter para continuar..."
            ;;
        0)  
            echo "Saliendo..."
            break
            ;;
        *)  
            echo "Opción inválida"
            read -p "Presioná Enter para continuar..."
            ;;
    esac
done