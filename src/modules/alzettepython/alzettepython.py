import sys
import ctypes
import numpy as np
from tabulate import tabulate

class AlzettePython_t:

    def __init__(self, values):
        self.values = values
        
        self.c = values[0]
        self.x = values[1]
        self.y = values[2]

    def alzette(self):
        self.x += self.rotate_bits(self.y,31)
        self.y ^= self.rotate_bits(self.x,24)
        self.x ^= self.c

        self.x += self.rotate_bits(self.y,17)
        self.y ^= self.rotate_bits(self.x,17)
        self.x ^= self.c

        self.x += self.rotate_bits(self.y,0)
        self.y ^= self.rotate_bits(self.x,31)
        self.x ^= self.c

        self.x += self.rotate_bits(self.y,24)
        self.y ^= self.rotate_bits(self.x,16)
        self.x ^= self.c

        return self.x, self.y

    def rotate_bits(self, bits, offset):
        return (bits >> offset)|(bits << (32 - offset)) & 0xFFFFFFFF

