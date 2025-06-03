# Guía de Trabajo Especial-A

**Integrantes del grupo**: Giménez García Daián, Gómez Rocío Guadalupe  
**Fecha**: 15 de junio de 2025  

---

## Resumen

El siguiente trabajo tiene por objetivo estudiar los siguientes métodos de generación de números pseudoaleatorios uniformes: Generador Congruencial Lineal, XORShift y Mersenne Twister. Para ello, se realiza en un inicio un análisis estadístico de tales RNGs (*Random Number Generators*), en el cual se evalúan distintas propiedades deseables de los mismos, como aleatoriedad, uniformidad, repetibilidad, entre otros.

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

## Descripción del problema:

### Detalles del método de simulación.
- La idea principal del método radica en generar durante 48 horas tanto el proceso de poisson que sería los momentos en que los clientes llegan, y los horarios de atención que siguen una distribución exponencial de parámetro lamda = 1/35. Por lo que en primera parte simulamos el proceso, guardamos todos los datos en un array y con el tamaño de ese array simulamos los horarios de atención y guardamos todos esos datos en otro array. 
Luego con esos dos arrays vamos calculando los demás datos, es decir


[1] Park, S. K., & Miller, K. W. (1988). Random number generators: Good ones are hard to find. *Communications of the ACM*, 31(10), 1192–1201. https://doi.org/10.1145/63039.63042

[2]  Marsaglia, George (July 2003). "Xorshift RNGs". Journal of Statistical Software.





