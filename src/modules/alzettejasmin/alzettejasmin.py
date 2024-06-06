import sys
import ctypes
import numpy as np

class AlzetteJasmin_t:

    def __init__(self, values):
        self.values = values

        self.c = values[0]
        self.x = values[1]
        self.y = values[2]

        self.load_library()

    def load_library(self):
        try:
            self.jasmin_alzette_dll = ctypes.cdll.LoadLibrary("./modules/alzettejasmin/alzette.so")
            sys.stdout.write("Alzette code successfully imported\n")
        except:
            sys.stdout.write("Couldn't import alzette.so library\nExiting\n")
            exit()

    def alzette(self):
        int32 = ctypes.c_int32
        args = [int32, int32, int32]
        self.jasmin_alzette_dll.alzette.argtypes = args

        padded_x = np.uint32(self.x)
        padded_y = np.uint32(self.y)
        padded_c = np.uint32(self.c)

        return_64 = self.jasmin_alzette_dll.alzette(padded_c, padded_x, padded_y)

        return_x = return_64 & 0xFFFF
        return_y = (return_64 >> 16) &  0xFFFF

        return return_x, return_y
