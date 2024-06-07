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
        offset_1 = [31, 17, 0, 24]
        offset_2 = [24, 17, 31, 16]

        for i in range(0, 4):   
            self.round(offset_1[i], offset_2[i])

        return self.x, self.y

    def round(self, offset_1, offset_2):
        self.x += self.rotate_bits(self.y, offset_1)
        self.y ^= self.rotate_bits(self.x, offset_2)
        self.x ^= self.c

    def rotate_bits(self, bits, offset):
        return (bits >> offset)|(bits << (32 - offset)) & 0xFFFFFFFF

