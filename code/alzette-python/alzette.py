import sys
import ctypes
import argparse

class Alzette:

    def __init__(self, c, x, y):
        self.c = c
        self.x = x 
        self.y = y
        self.launch_alzette()

    def launch_alzette(self):
        if parseur.args.python_alzette:
            if parseur.args.python_alzette == [0x67425301, 0xEDFCBA45, 0x98CBADFE]: 
                sys.stdout.write("NOTE: No value was given using the -p option. Alzette wil be run with default values:\n\t0x67425301, 0xEDFCBA45, 0x98CBADFE")
            self.result_x, self.result_y = self.python_alzette(self.x, self.y)
            if parseur.args.display:
                sys.stdout.write(f"Python Alzette ran successfully.\n\n\tHexa\n\t\tx={hex(self.x)}\n\t\ty={hex(self.y)}\n\n\tDecimal\n\t\tx={self.x}\n\t\ty={self.y}\n")
        elif parseur.args.jasmin_alzette:
            if parseur.args.jasmin_alzette == [0x67425301, 0xEDFCBA45, 0x98CBADFE]: 
                sys.stdout.write("NOTE: No value was given using the -j option. Alzette wil be run with default values:\n\t0x67425301, 0xEDFCBA45, 0x98CBADFE")
            self.load_library()
            self.jasmin_alzette(self.x, self.y)

    def load_library(self):
        try:
            ctypes.cdll.LoadLibrary("./alzette.so")
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

class Parseur:
    def __init__(self):
        self.parser = argparse.ArgumentParser(usage='python3 alzette.py [OPTIONS]', add_help=False, description='Python script to launch a Jasmins\' implementation of Alzette')
        self.parse_arguments()

    def parse_arguments(self):
        self.parser.add_argument('-h', '--help', action='help', help="shows this help message")
        self.parser.add_argument('-p', '--python_alzette', nargs=3, default = [0x67425301, 0xEDFCBA45, 0x98CBADFE], type = int, help="Launches Alzette (Python implementation)")
        self.parser.add_argument('-j', '--jasmin_alzette', nargs=3, default = [0x67425301, 0xEDFCBA45, 0x98CBADFE], type = int, help="Launches Alzette (Jasmin implementation)")
        self.parser.add_argument('-d', '--display', action='store_true', help="Display mode: displays results")

        self.args = self.parser.parse_args()

if __name__=="__main__":
    parseur = Parseur()
    if parseur.args.python_alzette:
        Alzette(parseur.args.python_alzette[0], parseur.args.python_alzette[1], parseur.args.python_alzette[2])
    elif parseur.args.jasmin_alzette:
        Alzette(parseur.args.jasmin_alzette[0], parseur.args.jasmin_alzette[1], parseur.args.jasmin_alzette[2])
