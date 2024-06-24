import sys
import ctypes
import os
import subprocess
from pathlib import Path
import numpy as np

class Argument(ctypes.Structure):
    _fields_ = [("arg_1", ctypes.c_int32),
                ("arg_2", ctypes.c_int32),
                ("arg_3", ctypes.c_int32),
                ("arg_4", ctypes.c_int32),
                ("arg_5", ctypes.c_int32),
                ("arg_6", ctypes.c_int32),
                ("arg_7", ctypes.c_int32),
                ("arg_8", ctypes.c_int32),]

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
        print("ok")

if __name__ == "__main__":
    SparkleInstance = SchwaemmJasmin_t()
    arg = Argument(1,2,3,4,5,6,7,8)
    ptr = ctypes.pointer(arg)
    SparkleInstance.sparkle(ptr)
    print(arg.arg_1)
    print(arg.arg_2)
    print(arg.arg_3)
    print(arg.arg_4)
    print(arg.arg_5)
    print(arg.arg_6)
    print(arg.arg_7)
    print(arg.arg_8)
    print("done")
