class LCG:
    def __init__(self, seed):
        self.a = 16807
        self.c = 0
        self.m = 2**31 - 1
        self.y = seed

    def next(self):
        self.y = (self.a * self.y + self.c) % self.m
        return self.y / self.m  # Número uniforme en [0, 1)


# Ejemplo de uso:
lcg = LCG(seed=12345)
for _ in range(10):
    print(lcg.next())
