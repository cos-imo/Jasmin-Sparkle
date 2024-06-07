import sys
import ctypes
import os
import subprocess
from pathlib import Path
import numpy as np

class AlzetteJasmin_t:

    def __init__(self, values):
        self.values = values

        self.c = values[0]
        self.x = values[1]
        self.y = values[2]

        self.load_library()

    def load_library(self):
        if Path("modules/alzettejasmin/alzette.so").exists():
            self.try_load()
            return
        else:
            sys.stdout.write("Alzette library (.so) not found. Would you like to try to compile it using make? (y/n) >>>")
            answer = input()
            if answer in ["y", "Y", "yes", "Yes"]:
                make = subprocess.run(["make", "-C", "modules/alzettejasmin/"], capture_output=True, text=True) 
                sys.stdout.write(f" === RUNNING MAKE === \n stdout:\n{make.stdout}\n ===================== \n\n\n")
                self.try_load()

    def try_load(self):
        try:
            self.jasmin_alzette_dll = ctypes.cdll.LoadLibrary("./modules/alzettejasmin/alzette.so")
            sys.stdout.write("Alzette code successfully imported\n")
        except:
            sys.stdout.write("Couldn't import alzette.so library\nExiting\n")
            exit()

    def alzette(self):
        int32 = ctypes.c_int32
        int64 = ctypes.c_int64

        args = [int32, int32, int32]
        self.jasmin_alzette_dll.alzette.argtypes = args
        self.jasmin_alzette_dll.alzette.restype = int64

        padded_x = np.uint32(self.x)
        padded_y = np.uint32(self.y)
        padded_c = np.uint32(self.c)

        return_64 = self.jasmin_alzette_dll.alzette(padded_c, padded_x, padded_y)

        return_x = return_64 & 0xFFFFFFFF
        return_y = (return_64 >> 32) & 0xFFFFFFFF

        return return_x, return_y
