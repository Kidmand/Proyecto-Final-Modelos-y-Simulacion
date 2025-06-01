# Comparación de Generadores de Números Pseudoaleatorios

## 🎯 Objetivo

Estudiar y comparar distintos métodos de generación de números pseudoaleatorios uniformes en el intervalo (0, 1), evaluando sus propiedades estadísticas, eficiencia y comportamiento en simulaciones.

---

## 🧪 Generadores analizados

- ✅ **Generador Congruencial Lineal (LCG)**  
  Parámetros: `a = 16807`, `c = 0`, `m = 2³¹ − 1`
- ✅ **XORShift**
- ✅ **Mersenne Twister (MT19937)**

---

## ⚙️ Propiedades evaluadas

Se tienen en cuenta las propiedades teóricas y prácticas deseables en un generador de números pseudoaleatorios:

| Propiedad                        | Descripción                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------ |
| 📈 **P1 (Aleatoriedad)**         | La secuencia debe ser intuitivamente aleatoria (no predecible visualmente).          |
| 📊 **P2 (Test de aleatoriedad)** | Debe pasar tests estadísticos para garantizar distribución uniforme e independencia. |
| 📚 **P3 (Conocimiento teórico)** | Se debe conocer la estructura del generador para garantizar confiabilidad.           |
| ♻️ **Repetibilidad**             | Mismo seed → misma secuencia. Permite reproducibilidad en simulaciones.              |
| ⚡ **Velocidad**                 | Evaluar el rendimiento al generar grandes volúmenes de números.                      |

---

## 📋 Pasos del análisis comparativo

### 1. 🔧 Implementación

- Se implementan o utilizan bibliotecas que permiten acceder al funcionamiento interno de los generadores.

### 2. 🔁 Repetibilidad (P3)

- Generar dos secuencias con el mismo `seed` y verificar que sean iguales.

### 3. 📈 Test de Uniformidad (P2, propiedad 1)

- Generar `N = 100.000` números.
- Calcular:
  - Media (esperada ≈ 0.5)
  - Varianza (esperada ≈ 1/12 ≈ 0.0833)
- Visualizar con histogramas.
- Aplicar test de **Kolmogorov–Smirnov** o **Chi-cuadrado**.

### 4. 🔗 Test de Independencia (P2, propiedad 2)

- Graficar pares de números consecutivos \((u*i, u*{i+1})\)
- Calcular la autocorrelación (esperada ≈ 0).
- _(Opcional)_ Analizar tríos \((u*i, u*{i+1}, u\_{i+2})\) en un cubo 3D.

### 5. ⏱️ Velocidad

- Medir el tiempo necesario para generar 1 millón de números con cada generador.

## 📊 Resultados esperados

Al final se construye una tabla comparativa como la siguiente:

| Generador | Repetible | Media | Varianza | KS/Chi² Test | Autocorrelación | Tiempo (s) |
| --------- | --------- | ----- | -------- | ------------ | --------------- | ---------- |
| LCG       | Sí        | 0.499 | 0.0834   | ✔️           | ≈ 0             | 0.12       |
| XORShift  | Sí        | 0.501 | 0.0832   | ✔️           | ≈ 0             | 0.05       |
| MT19937   | Sí        | 0.500 | 0.0833   | ✔️           | ≈ 0             | 0.10       |

---
