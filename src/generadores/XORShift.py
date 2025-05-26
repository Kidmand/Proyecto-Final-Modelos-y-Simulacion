class XORShift:

    def __init__(self, seed):
        self.a = 1
        self.b = 21
        self.c = 20
        self.y = seed

    def generate(self):
        self.y ^= (self.y << self.a) & 0xFFFFFFFF
        self.y ^= (self.y >> self.b) 
        self.y ^= (self.y << self.c) & 0xFFFFFFFF
        return self.y 
    
def main():
    rng = XORShift(2463534242)
    for _ in range(10):
        print(rng.generate())

if __name__ == '__main__':
    main()
