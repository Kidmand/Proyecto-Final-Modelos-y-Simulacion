# Simulación de sistema de colas

Este proyecto tiene como objetivo comparar distintos generadores de números pseudoaleatorios uniformes mediante análisis estadístico y aplicarlos a un sistema de colas con un solo servidor.

El trabajo se realiza como parte de la materia **Modelos y Simulación** (Primer cuatrimestre de 2025, U.N.C).

## Generadores implementados

- **Generador congruencial lineal (LCG)**
- **XORShift**
- **Mersenne Twister (MT19937)**

## Problema simulado

Se simula un sistema de colas donde:

- Las llegadas siguen un proceso de Poisson no homogéneo con intensidad:  
  λ(t) = 20 + 10·cos(πt/12) (clientes por hora)
- Los tiempos de atención son exponenciales con tasa μ = 35 (clientes por hora)
- El servidor atiende por orden de llegada y no hay límite de espera

La simulación abarca un período de **48 horas**.

## Estructura del proyecto

```
simulacion-colas/
│
├── src/                                  # Código fuente Python
│   ├── analisis/                         # Scripts de análisis de resultados
│   │   ├── Analisis_generadores.py
│   │   ├── Analisis_simulacion.py
│   │   └── Medir_tiempos.py
│   ├── generadores/                      # Implementación de generadores
│   │   ├── LCG.py
│   │   ├── MersenneTwister.py
│   │   └── XORShift.py
│   ├── test/                             # Tests automatizados
│   │   ├── test_generadores.py
│   │   └── test_simulacion.py
│   └── Simulacion.py                     # Simulación del sistema de colas
│
├── results/                              # Resultados de simulación
│   ├── graficos/                         # Imágenes generadas
│   │   ├── generadores/                  # Gráficos de análisis de generadores
│   │   │   ├── Cubo_LCG.png
│   │   │   ├── Cubo_MersenneTwister.png
│   │   │   ├── Cubo_XORShift.png
│   │   │   ├── Histograma_LCG.png
│   │   │   ├── Histograma_MersenneTwister.png
│   │   │   ├── Histograma_XORShift.png
│   │   │   ├── Pares_LCG.png
│   │   │   ├── Pares_MersenneTwister.png
│   │   │   └── Pares_XORShift.png
│   │   ├── simulacion/                   # Gráficos relacionados a la simulación
│   │   │   ├── Arribos_LCG.png
│   │   │   ├── Arribos_MersenneTwister.png
│   │   │   ├── Arribos_XORShift.png
│   │   │   ├── Espera_LCG.png
│   │   │   ├── Espera_MersenneTwister.png
│   │   │   ├── Espera_XORShift.png
│   │   │   ├── Longitud_LCG.png
│   │   │   ├── Longitud_MersenneTwister.png
│   │   │   ├── Longitud_XORShift.png
│   │   │   ├── Servicios_LCG.png
│   │   │   ├── Servicios_MersenneTwister.png
│   │   │   ├── Servicios_XORShift.png
│   │   │   ├── Uso_LCG.png
│   │   │   ├── Uso_MersenneTwister.png
│   │   │   └── Uso_XORShift.png
│   └── reportes/                         # Documentación y entregables
│       ├── Informe.md
│       ├── Pasos_a_seguir.md
│       └── A - Trabajo Práctico Especial.pdf
│
├── requirements.txt                      # Dependencias del proyecto
├── README.md                             # Descripción general del proyecto
├── run.sh                                # Script para correr análisis y simulación
└── .gitignore                            # Archivos ignorados por Git


```

## Instalación y ejecución

Se recomienda usar un entorno virtual para evitar conflictos de dependencias.

### 1. Clonar el repositorio

```bash
git clone git@github.com:TU_USUARIO/simulacion-colas.git
cd simulacion-colas
```

### 2. Crear y activar un entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate      # Linux/macOS
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el script y seleccionar la opción que desee del menú

```bash
./run.sh
```
## Informe
El informe se encuentra en 
```bash
results/reportes/informe.md
```
## Licencia

Este proyecto es de uso académico y puede reutilizarse con fines educativos.
