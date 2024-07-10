import sys
import ctypes
import numpy as np

import modules.alzettepython.alzettepython as AlzettePython 
import modules.alzettejasmin.alzettejasmin as AlzetteJasmin 

import modules.craxjasmin.craxjasmin as CraxJasmin 
import modules.craxjasmin.craxjasmin as CraxJasmin 

import modules.schwaemmjasmin.schwaemmjasmin as SchwaemmJasmin 
#import modules.schwaemmpython.schwaemmpython as SchwaemmPython

import modules.tests.testmanager

from tabulate import tabulate

class CoreLauncher:

    def __init__(self, parseur, values):
        self.parseur = parseur
        self.values = [np.uint32(element) for element in values]
        self.core()

    def core(self):
        self.check_values()
        if self.parseur.args.python_alzette:
            alzettePython = AlzettePython.AlzettePython_t()
            self.result_x_python, self.result_y_python = alzettePython.alzette(self.values[0], self.values[1], self.values[2])
            print(f"{self.result_x_python, self.result_y_python}")

        if self.parseur.args.jasmin_alzette:
            alzetteJasmin = AlzetteJasmin.AlzetteJasmin_t()
            self.result_x_jasmin, self.result_y_jasmin = alzetteJasmin.alzette(self.values[0], self.values[1], self.values[2])
            print(f"{self.result_x_jasmin}, {self.result_y_jasmin}")

        if self.parseur.args.crax_jasmin:
            craxJasmin = CraxJasmin.CraxJasmin_t()
            self.result_x_crax, self.result_y_crax = craxJasmin.crax(self.values[0], self.values[1], self.values[2])
            print(f"{self.result_x_crax}  {self.result_y_crax}")

        if self.parseur.args.schwaemm_jasmin:
            schwaemmJasmin = SchwaemmJasmin.SchwaemmJasmin_t()
            self.result_x_schwaemm, self.result_y_schwaemm = schwaemmJasmin.schwaemm()
            print(f"{self.result_x_schwaemm}  {self.result_y_schwaemm}")

        if self.parseur.args.test:
            modules.tests.testmanager.testmanager_t(self.parseur.args.test, self.parseur.args.python_alzette, self.parseur.args.jasmin_alzette, self.values)

        if self.parseur.args.display:
            self.display()

    def check_values(self):
        if self.values == [0x67425301, 0xEDFCBA45, 0x98CBADFE]: 
            sys.stdout.write(f"NOTE: No value was given in arguments. Alzette wil be run with default values:\n\t0x67425301, 0xEDFCBA45, 0x98CBADFE")

    def display(self):
        if hasattr(self, 'result_x_python'):
            sys.stdout.write(f"Python Alzette ran successfully.\n\n\tHexa\n\t\tx={hex(self.result_x_python)}\n\t\ty={hex(self.result_y_python)}\n\n\tDecimal\n\t\tx={self.result_x_python}\n\t\ty={self.result_y_python}\n")
        if hasattr(self, 'result_x_jasmin'):
            sys.stdout.write(f"Jasmin Alzette ran successfully.\n\n\tHexa\n\t\tx={hex(self.result_x_jasmin)}\n\t\ty={hex(self.result_y_jasmin)}\n\n\tDecimal\n\t\tx={self.result_x_jasmin}\n\t\ty={self.result_y_jasmin}\n")

