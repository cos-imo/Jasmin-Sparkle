import sys
import ctypes
import os
import subprocess
from pathlib import Path
import numpy as np

class SchwaemmJasmin_t:

    def __init__(self):

        self.load_library()

    def load_library(self):
        if Path("modules/schwaemmjasmin/schwaemm.so").exists():
            self.try_load()
            return
        else:
            sys.stdout.write("Schwaemm library (.so) not found. Would you like to try to compile it using make? (y/n) >>>")
            answer = input()
            if answer in ["y", "Y", "yes", "Yes"]:
                make = subprocess.run(["make", "-C", "modules/schwaemmjasmin/"], capture_output=True, text=True) 
                sys.stdout.write(f" === RUNNING MAKE === \n stdout:\n{make.stdout}\n ===================== \n\n\n")
                self.try_load()

    def try_load(self):
        try:
            self.jasmin_schwaemm_dll = ctypes.cdll.LoadLibrary("./modules/schwaemmjasmin/schwaemm.so")
        except:
            sys.stdout.write("Couldn't import schwaem.so library\nExiting\n")
            exit()

    def schwaemm(self):
        int32 = ctypes.c_int32
        int64 = ctypes.c_int64

        args = [int32, int32, int32, int32, int32, int32]

        return_64 = self.jasmin_schwaemm_dll.schwaemm()

        return_y = return_64 & 0xFFFFFFFF
        return_x = (return_64 >> 32) & 0xFFFFFFFF

        return return_x, return_y
        #self.jasmin_crax_dll.crax.argtypes = args
        #self.jasmin_crax_dll.crax.restype = int64
"""
        padded_x = np.uint32(x)
        padded_y = np.uint32(y)
        padded_key_0 = np.uint32(key_0)
        padded_key_1 = np.uint32(key_1)
        padded_key_2 = np.uint32(key_2)
        padded_key_3 = np.uint32(key_3)

"""
