# Simulación de sistema de colas

## Estructura del proyecto

```
simulacion-colas/
│
├── src/                         # Código fuente Python
│   ├── generadores/             # Implementación de generadores
│   │   ├── lcg.py
│   │   ├── xorshift.py
│   │   └── pcg.py
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
