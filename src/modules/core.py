import sys
import ctypes
import numpy as np

import modules.alzettepython.alzettepython as AlzettePython 
import modules.alzettejasmin.alzettejasmin as AlzetteJasmin 

import modules.tests.testmanager

from tabulate import tabulate

class CoreLauncher:

    def __init__(self, parseur, values):
        self.parseur = parseur
        self.values = values
        self.core()

    def core(self):
        self.check_values()
        if self.parseur.args.python_alzette:
            alzettePython = AlzettePython.AlzettePython_t(self.values)
            self.result_x_python, self.result_y_python = alzettePython.alzette()

        if self.parseur.args.jasmin_alzette:
            alzetteJasmin = AlzetteJasmin.AlzetteJasmin_t(self.values)
            self.result_x_jasmin, self.result_y_jasmin = alzetteJasmin.alzette()

        if self.parseur.args.test:
            modules.tests.testmanager.testmanager_t(self.parseur.args.test, self.parseur.args.python_alzette, self.parseur.args.jasmin_alzette)

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

