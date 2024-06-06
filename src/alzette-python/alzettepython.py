import sys
import ctypes
import numpy as np
from tabulate import tabulate

class Alzette:

    def __init__(self, parseur, c, x, y):
        self.c = c
        self.x = x 
        self.y = y
        self.parseur = parseur
        self.launch_alzette()

    def launch_alzette(self):
        if self.parseur.args.python_alzette:
            if self.parseur.args.python_alzette == [0x67425301, 0xEDFCBA45, 0x98CBADFE]: 
                sys.stdout.write("NOTE: No value was given using the -p option. Alzette wil be run with default values:\n\t0x67425301, 0xEDFCBA45, 0x98CBADFE")
            self.result_x, self.result_y = self.python_alzette(self.x, self.y)
            if self.parseur.args.display:
                sys.stdout.write(f"Python Alzette ran successfully.\n\n\tHexa\n\t\tx={hex(self.x)}\n\t\ty={hex(self.y)}\n\n\tDecimal\n\t\tx={self.x}\n\t\ty={self.y}\n")
        elif self.parseur.args.jasmin_alzette:
            if self.parseur.args.jasmin_alzette == [0x67425301, 0xEDFCBA45, 0x98CBADFE]: 
                sys.stdout.write("NOTE: No value was given using the -j option. Alzette wil be run with default values:\n\t0x67425301, 0xEDFCBA45, 0x98CBADFE")
            self.load_library()
            self.jasmin_alzette(self.c, self.x, self.y)
        if self.parseur.args.test:
            self.test(self.x, self.y)

    def load_library(self):
        try:
            self.jasmin_alzette_dll = ctypes.cdll.LoadLibrary("./alzette-python/alzette.so")
            sys.stdout.write("Alzette code successfully imported\n")
        except:
            sys.stdout.write("Couldn't import alzette.so library\nExiting\n")
            exit()


    def python_alzette(self, x, y):
        x += self.rotate_bits(y,31)
        y ^= self.rotate_bits(x,24)
        x ^= self.c

        x += self.rotate_bits(y,17)
        y ^= self.rotate_bits(x,17)
        x ^= self.c

        x ^= self.rotate_bits(y,0)
        y ^= self.rotate_bits(x,31)
        x ^= self.c

        x += self.rotate_bits(y,24)
        y ^= self.rotate_bits(x,16)
        x ^= self.c

        return x,y

    def jasmin_alzette(self, x, y):
        # arguments: c_int32
        int32 = ctypes.c_int32
        args = [int32, int32, int32]
        self.jasmin_alzette_dll.alzette.argtypes = args

        padded_x = np.uint32(x)
        padded_y = np.uint32(y)
        padded_c = np.uint32(self.c)

        return_64 = self.jasmin_alzette_dll.alzette(padded_c, padded_x, padded_y)

        return_x = return_64 & 0xFFFF
        return_y = (return_64 >> 16) &  0xFFFF

        return return_x, return_y
        
    def test(self, x, y):
        self.load_library()

        python_x, python_y = self.python_alzette(x, y)
        jasmin_x, jasmin_y = self.jasmin_alzette(x,y)

        print(tabulate([["x", python_x, jasmin_x, ["non ok", "ok"][python_x == jasmin_x]], ["y",python_y, jasmin_y, ["non ok", "ok"][python_x == jasmin_x]]], ["variable","python", "jasmin", "test"], tablefmt="grid"))

    def rotate_bits(self, bits, offset):
        return (bits >> offset)|(bits << (32 - offset)) & 0xFFFFFFFF

