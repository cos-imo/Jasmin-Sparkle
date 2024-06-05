import sys
import ctypes

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
            self.jasmin_alzette(self.x, self.y)

    def load_library(self):
        try:
            ctypes.cdll.LoadLibrary("./alzette-python/alzette.so")
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

    def rotate_bits(self, bits, offset):
        return (bits >> offset)|(bits << (32 - offset)) & 0xFFFFFFFF

