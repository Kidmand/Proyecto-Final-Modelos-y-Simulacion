# Guía de Trabajo Especial-A

**Integrantes del grupo**: Giménez García Daián, Gómez Rocío Guadalupe  
**Fecha**: 15 de junio de 2025

---

## Resumen

El siguiente trabajo tiene por objetivo estudiar los siguientes métodos de generación de números pseudoaleatorios uniformes: Generador Congruencial Lineal, XORShift y Mersenne Twister. Para ello, se realiza en un inicio un análisis estadístico de tales RNGs (_Random Number Generators_), en el cual se evalúan distintas propiedades deseables de los mismos, como aleatoriedad, uniformidad, repetibilidad, entre otros.

A continuación, se los aplica a un problema concreto: una simulación de un sistema de colas de un solo servidor en donde los arribos de los clientes sigue un proceso de Poisson no homogéneo y los tiempos de atención un distribución exponencial. Finalmente, analizamos cómo impacta cada método en el comportamiento observado en la simulación.

---

## Descripción teórica de los generadores

### 1. Generador Congruencial Lineal (LCG)

**Fórmula general:**  
yₙ = (a · yₙ₋₁ + c) mod M, con n ≥ 1, para M un entero positivo tal que M ≥ 2.

**Parámetros:**  
Los parámetros del generador son a, c, M y la semilla y₀, donde a, c y y₀ son enteros del conjunto {0, ..., M-1}.

Esto genera una sucesión y₁, y₂, ..., yₙ, ... con valores en el conjunto {0, 1, ..., M-1}.

**Parámetros utilizados:**

- a = 16807
- c = 0
- m = 2³¹ - 1
- y₀ = 12345

Como se busca una secuencia de números aleatorios en el intervalo (0,1), se toma:  
Uₙ = yₙ / M

**Calidad esperada**:  
Este generador, con los parámetros seleccionados (`a = 16807`, `c = 0`, `M = 2^{31} - 1`), corresponde al generador de Lehmer, el cual es reconocido por su buena calidad estadística. [1]

Presenta un **período máximo de \( M - 1 \)**, lo cual nos garantiza una secuencia extensa antes de repetir valores. Por ello,se anticipa un desempeño adecuado en simulaciones que requieran números pseudoaleatorios uniformemente distribuidos, como las utilizadas en este trabajo.

### 2. XORShift

**Fórmula general:**  
El algoritmo XORShift genera números pseudoaleatorios aplicando una secuencia de operaciones XOR y desplazamientos de bits a un valor semilla. En su forma más simple (propuesta por George Marsaglia en 2003), se define como:

```c
x ^= x << a;
x ^= x >> b;
x ^= x << c;
```

donde `x` es el estado interno (semilla), `<<` y `>>` son desplazamientos de bits a izquierda y derecha, y `^` es la operación XOR bit a bit.

**Teoría matemática del generador XORShift [2]**

Un modelo matemático aplicable a la mayoría de los RNGs (generadores de números aleatorios) es el siguiente:

Se tiene un conjunto de semillas Z compuesto de m-úplas (x₁, ..., xₘ) y una función inyectiva f definida sobre Z. Al elegir z de manera uniforme y aleatoria de Z, la secuencia generada por el RNG es:

    f(z), f(f(z)), f(f(f(z))), ...

Esta secuencia no es independiente, pero sí se encuentra distribuida de manera uniforme sobre el conjunto Z.

Para el XORShift de 32 bits implementado, el conjunto Z es el conjunto de vectores binarios 1 × 32, excluyendo al vector nulo, y la función f está representada por una matriz binaria no singular 32 × 32, denotada por T.

Si B es un vector binario elegido de Z de forma aleatoria y uniforme, entonces se genera la secuencia:

BT, BT², BT³, ...

la cual también está uniformemente distribuida sobre Z.

Consideramos ahora la matriz I + Lᵃ, donde L es la matriz 32 × 32 con todos sus elementos en cero, excepto por unos en la subdiagonal principal. Esta matriz implementa la operación de **desplazamiento a la izquierda** (left shift), y la suma + es la suma módulo 2 (XOR).

De forma similar, podemos tomar I + Rᵇ, donde R es la matriz traspuesta de L, la cual implementa el **desplazamiento a la derecha** (right shift). Nuevamente, el símbolo + denota suma módulo 2.

Ambas matrices I + Lᵃ e I + Rᵇ son no singulares.

Si tomamos:

T = (I + Lᵃ)(I + Rᵇ)(I + Rᶜ)

con parámetros a, b, c adecuados, podemos construir una matriz de orden 2³² - 1, lo cual garantiza un período máximo para la secuencia generada.

**Parámetros Usados:**

- \( a = 1 \)
- \( b = 21 \)
- \( c = 20 \)

- \( x = 12345 \)

Estos valores corresponden a una de las tuplas recomendadas en el artículo original de Marsaglia.

---

### 3. Mersenne Twister

**Parámetros del Algoritmo General del Mersenne Twister**

El algoritmo general del Mersenne Twister se caracteriza por las siguientes cantidades:

- `w`: tamaño de palabra (en bits)
- `n`: grado de recurrencia
- `m`: palabra intermedia, un desplazamiento usado en la relación de recurrencia que define la serie `x`, con `1 ≤ m < n`
- `r`: punto de separación de una palabra, o número de bits de la máscara de bits inferiores, con `0 ≤ r ≤ w - 1`
- `a`: coeficientes de la twist matrix en forma racional normal
- `b`, `c`: máscaras de bits de atenuación (tempering) TGFSR(R)
- `s`, `t`: desplazamientos de bits de atenuación TGFSR(R)
- `u`, `d`, `l`: desplazamientos y máscaras de bits adicionales de atenuación del Mersenne Twister

Con la restricción de que $2^{ n * w - r} - 1$ sea un primo de Mersenne.

**Parámetros concretos del Mersenne Twister (MT19937)**

- `(w, n, m, r) = (32, 624, 397, 31)`
- `a = 0x9908B0DF`
- `(u, d) = (11, 0xFFFFFFFF)`
- `(s, b) = (7, 0x9D2C5680)`
- `(t, c) = (15, 0xEFC60000)`
- `l = 18`

**Fórmula General**

El Mersenne Twister genera una secuencia de números a partir de una recurrencia lineal sobre un campo finito binario $\mathbb{F}_2$.

La idea general es definir una sucesión $x_{i}$ mediante una relación de recurrencia sencilla y luego devolver números de la forma $x_{i}^T$ donde $T$ es una matriz invertible en $\mathbb{F}_2$ (llamada _tempering matrix_).

Esta sucesión se define como:

$$
x_{k+n} = x_{k+m} \oplus \left( (x_k^u \,\|\, x_{k+1}^l) \cdot A \right)
$$

con k = 0, 1, 2...

- $x_{k}$: k-ésimo número del estado interno (32 bits)
- $(x_k^u \,\|\, x_{k+1}^l)$: combinación de los bits altos de `x[k]` y los bajos de `x[k+1]`
- $A$ : matriz de transformación lineal
- ⊕ : operación XOR

La transformación _twist_ usa la matriz $A$ que se define como:

$
A =
\begin{pmatrix}
0 & I_{w-1} \\
a_{w-1} & (a_{w-2}, \dots, a_0)
\end{pmatrix}
$

- $I_{w-1}$ : matriz identidad de tamaño $(w-1) × (w-1)$

Esto permite expresar la multiplicación por A de la siguente forma:

    Si x_0 = 0: x · A = x >> 1

    Si x_0 = 1: x · A = (x >> 1) ⊕ a

donde $x_{0}$ es el bit menos significativo de x.

Para T (tempering matrix) como queremos que sea fácilmente computable, por lo que no se la construye directamente. En el caso del Mersenne Twister, esta transformación se define como sigue:

    y = x ^ ((x >> u) & d)

    y = y ^ ((y << s) & b)

    y = y ^ ((y << t) & c)

    z = y ^ (y >> l)

Donde:

- `x` es el siguiente valor de la serie generada,
- `y` es un valor intermedio temporal,
- `z` es el valor final devuelto por el algoritmo,
- `>>` y `<<` son desplazamientos binarios a la derecha e izquierda, respectivamente,
- `&` es la operación AND bit a bit,
- `^` representa XOR bit a bit.

## Descripción del problema

El objetivo de este trabajo es simular un sistema de colas con un único servidor, donde los clientes llegan en distintos momentos y son atendidos en orden de llegada. La particularidad del problema radica en que la tasa de llegada de clientes varía con el tiempo, mientras que los tiempos de atención siguen una distribución aleatoria fija.

### Características del sistema:

- **Llegadas**: siguen un proceso de Poisson no homogéneo, con una tasa que varía a lo largo del tiempo según la función:

  $
  \lambda(t) = 20 + 10 \cdot \cos\left(\frac{\pi t}{12}\right)
  $

  Esta expresión indica que los clientes llegan con mayor frecuencia en ciertos momentos del día, imitando situaciones reales como las horas pico.

- **Atención**: los tiempos de servicio de los clientes siguen una distribución exponencial con tasa fija:

  $
  \mu = 35 \text{ clientes/hora}
  $

- **Condiciones del sistema**:
  - Un solo servidor atiende a los clientes por orden de llegada.
  - No hay un límite en la cantidad de clientes que pueden esperar en la cola.
  - La simulación abarca un período total de 48 horas.

Esta configuración permite observar cómo se comporta el sistema a lo largo del tiempo y comparar el impacto que tiene el uso de diferentes generadores de números aleatorios.

## Metodología

Para evaluar la calidad y el impacto de los generadores seleccionados (LCG, XORShift y Mersenne Twister), se implementaron una serie de pruebas estadísticas y una simulación completa del sistema de colas. El enfoque se dividió en dos partes principales:

### 1. Tests de calidad de los generadores

Se desarrollaron pruebas automatizadas en Python utilizando la biblioteca `pytest`, con el fin de comprobar algunas propiedades básicas deseables en los generadores:

- **Repetibilidad**: Se comprobó que los generadores producen siempre la misma secuencia si se les da la misma semilla. Esto es fundamental para asegurar que los experimentos puedan repetirse.
- **Uniformidad**: Se generaron 100.000 valores con cada generador. Se calcularon la media y la varianza empíricas, y se compararon con los valores teóricos de una distribución uniforme U(0,1) (esperando una media ≈ 0.5 y varianza ≈ 1/12).

### 2. Simulación del sistema de colas

Para analizar el comportamiento del sistema bajo cada generador, se simuló el proceso completo de atención durante 48 horas. La simulación consistió en:

- **Generación de arribos**: Se usó el método de _thinning_ para simular un proceso de Poisson no homogéneo. Se generan candidatos usando una tasa constante máxima (`λ_max = 30`), y se aceptan con probabilidad proporcional a la tasa real λ(t).
- **Generación de servicios**: Los tiempos de atención se obtienen aplicando la transformación inversa a números uniformes generados, para simular una distribución exponencial con parámetro μ = 35.

- **Modelo de atención**: Se simula el comportamiento del servidor minuto a minuto. En cada paso, se decide si el cliente debe esperar (si llegó antes de que el servidor esté libre) o si puede ser atendido inmediatamente. También se registra cuánto tiempo estuvo libre el servidor antes de la llegada de un nuevo cliente.

Se utilizaron arrays para almacenar:

- Tiempos de llegada,
- Tiempos de atención,
- Tiempos de espera por parte de los clientes,
- Períodos en los que el servidor estuvo ocioso,
- Evolución de la longitud de la cola.

Estos datos luego se procesan para calcular métricas globales, como el porcentaje de tiempo ocupado, la longitud media de la cola, y el tiempo promedio en el sistema. Además, se generan gráficos e histogramas para observar visualmente el comportamiento del sistema bajo cada generador.

---

[1] Park, S. K., & Miller, K. W. (1988). Random number generators: Good ones are hard to find. _Communications of the ACM_, 31(10), 1192–1201. https://doi.org/10.1145/63039.63042

[2] Marsaglia, George (July 2003). "Xorshift RNGs". Journal of Statistical Software.
