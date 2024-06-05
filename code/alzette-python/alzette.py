import sys

class Alzette:

    def __init__(self, c, x, y):
        self.c = c
        x, y = self.alzette(x,y)

        sys.stdout.write(f"Alzette ran successfully.\n\n\tHexa\n\t\tx={hex(x)}\n\t\ty={hex(y)}\n\n\tDecimal\n\t\tx={x}\n\t\ty={y}\n")

    def alzette(self, x, y):
        x += (y>>31)
        y ^= (x>>24)
        x ^= self.c

        x += (y>>17)
        y ^= (x>>17)
        x ^= self.c

        x ^= (y>>0)
        y ^= (x>>31)
        x ^= self.c

        x += (y>>24)
        y ^= (x>>16)
        x ^= self.c

        return x,y


if __name__=="__main__":
    Alzette(0xb7e15162, 0x9e3779b9, 0x6e3449b3)
