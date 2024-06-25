import sys
import ctypes
import os
import subprocess
from pathlib import Path
import numpy as np

class Argument(ctypes.Structure):
    _fields_ = [("arg_array", ctypes.c_int32 * 8)]

class SchwaemmJasmin_t:

    def __init__(self):

        self.load_library()

    def load_library(self):
        if Path("sparkle.so").exists():
            self.try_load()
            return
        else:
            sys.stdout.write("Sparkle library (.so) not found. Please compile it.\nExiting\n")
            exit()

    def try_load(self):
        try:
            self.jasmin_sparkle_dll = ctypes.cdll.LoadLibrary("sparkle.so")
        except:
            sys.stdout.write("Couldn't import sparkle.so library\nExiting\n")
            exit()

    def sparkle(self, arg):
        args = [ctypes.POINTER(Argument)]

        self.jasmin_sparkle_dll.sparkle.argtypes = args
        self.jasmin_sparkle_dll.sparkle.restype = None
        self.jasmin_sparkle_dll.sparkle(arg)

if __name__ == "__main__":
    SparkleInstance = SchwaemmJasmin_t()
    ints = ctypes.c_int32 * 8
    array = ints(1,2,3,4,5,6,7,8)
    arg = Argument(array)
    ptr = ctypes.pointer(arg)
    SparkleInstance.sparkle(ptr)

    for i in range(0,4):
        value = array[i]
        value1 = value & 0xFF
        value2 = value
        value2  = (value2 >> 16) & 0xFFFFFFFF 
        value2 = value2 & 0xFF
        print(f"x_{i*2} : {value1}\tx_{i*2+1} : {value2}")

