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
        int64 = ctypes.c_int64

        args = [int64]

        return_var = self.jasmin_schwaemm_dll.schwaemm()

        return return_var
