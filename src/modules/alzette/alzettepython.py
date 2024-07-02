import sys
import ctypes
import numpy as np
from tabulate import tabulate

class AlzettePython_t:

    def __init__(self):
        pass

    def alzette(self, c, x, y):
        self.c = np.uint32(c)
        self.x = np.uint32(x)
        self.y = np.uint32(y)

        offset_1 = [31, 17, 0, 24]
        offset_2 = [24, 17, 31, 16]

        offset_1 = [np.uint32(element) for element in offset_1]
        offset_2 = [np.uint32(element) for element in offset_2]

        for i in range(0, 4):   
            self.round(offset_1[i], offset_2[i])

        return np.uint32(self.x), np.uint32(self.y)

    def round(self, offset_1, offset_2):
        self.x += self.rotate_bits(self.y, offset_1)
        self.y ^= self.rotate_bits(self.x, offset_2)
        self.x ^= self.c
        self.x = np.uint32(self.x)

    def rotate_bits(self, bits, offset):
        return np.uint32(np.uint32((bits >> offset))|np.uint32((bits << (32 - offset))) & 0xFFFFFFFF)

