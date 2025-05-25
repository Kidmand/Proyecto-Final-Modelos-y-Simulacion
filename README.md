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
├── src/                         # Código fuente Python
│   ├── generadores/             # Implementación de generadores
│   │   ├── lcg.py
│   │   ├── xorshift.py
│   │   └── MerTwi.py
│   ├── test_generadores.py      # Script para comparar los generadores
│   └── simulacion.py            # (Más adelante) simulación del sistema de colas
│
├── results/                     # Resultados de simulación
│   ├── graficos/                # Imágenes generadas
│   │   ├── uso_servidor.png
│   │   ├── tiempos_espera_hist.png
│   └── reportes/                # Informes exportados
│       └── informe.pdf
│
├── requirements.txt             # Librerías necesarias
├── README.md                    # Descripción general del proyecto
└── .gitignore                   # Archivos a ignorar por Git

```

## Instalación y ejecución

Se recomienda usar un entorno virtual para evitar conflictos de dependencias.

### 1. Clonar el repositorio

```bash
git clone git@github.com:TU_USUARIO/simulacion-colas.git
cd simulacion-colas
```

### 2. Crear y activar un entorno virtual
python3 -m venv venv
source venv/bin/activate      # Linux/macOS

### 3. Instalar dependencias
pip install -r requirements.txt

### 4. Ejecutar los scripts
python src/test_generadores.py       # Para testear los generadores
python src/simulacion.py             # Para ejecutar la simulación principal


## Licencia

Este proyecto es de uso académico y puede reutilizarse con fines educativos.

