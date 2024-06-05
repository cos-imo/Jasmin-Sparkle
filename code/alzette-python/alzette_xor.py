import sys
from operator import xor as xor
import numpy as np

class Alzette:

    def __init__(self, c, x, y):
        self.c = c
        x, y = self.alzette(x,y)

        sys.stdout.write(f"Alzette ran successfully.\n\n\tHexa\n\t\tx={hex(x)}\n\t\ty={hex(y)}\n\n\tDecimal\n\t\tx={x}\n\t\ty={y}\n")

    def alzette(self, x, y):
        x += (y>>31)
        y = xor(y, (x>>24))
        x = xor(x, self.c)

        x += (y>>17)
        xor(y, (x>>17))
        xor(x, self.c)

        xor(x, y>>0)
        xor(y, x>>31)
        xor(x, self.c)

        x += (y>>24)
        xor(y, x>>16)
        xor(x, self.c)

        return x,y


if __name__=="__main__":
    Alzette(0xb7e15162, 0x9e3779b9, 0x6e3449b3)
