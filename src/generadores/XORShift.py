class XORShift:

    def __init__(self, seed):
        self.a = 1
        self.b = 21
        self.c = 20
        self.y = seed
        self.max_val = 2**32 - 1

    def generate(self):
        self.y ^= (self.y << self.a) & 0xFFFFFFFF
        self.y ^= (self.y >> self.b)
        self.y ^= (self.y << self.c) & 0xFFFFFFFF
        return self.y

    def random(self):
        return self.generate() / float(self.max_val)


def main():
    rng = XORShift(182374)
    for _ in range(10):
        print(rng.random())


if __name__ == '__main__':
    main()
