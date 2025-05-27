class LCG:
    def __init__(self, seed):
        self.a = 16807
        self.c = 0
        self.m = 2**31 - 1
        self.y = seed

    def random(self):
        self.y = (self.a * self.y + self.c) % self.m
        return self.y / self.m  # Número uniforme en [0, 1)


# Ejemplo de uso:
if __name__ == '__main__':
    lcg = LCG(12345)
    for _ in range(10):
        print(lcg.random())
