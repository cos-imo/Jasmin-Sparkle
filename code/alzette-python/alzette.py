import sys
import ctypes
import argparse

class Alzette:

    def __init__(self, c, x, y):
        self.load_library()
        self.c = c
        x, y = self.alzette(x,y)

        sys.stdout.write(f"Alzette ran successfully.\n\n\tHexa\n\t\tx={hex(x)}\n\t\ty={hex(y)}\n\n\tDecimal\n\t\tx={x}\n\t\ty={y}\n")

    def load_library(self):
        try:
            ctypes.cdll.LoadLibrary("./alzette.so")
            sys.stdout.write("Alzette code successfully imported\n")
        except:
            sys.stdout.write("Couldn't import alzette.so library\nExiting\n")
            exit()


    def alzette(self, x, y):
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
        self.parser = argparse.ArgumentParser(usage='python3 alzette.py [OPTIONS]', add_help=False, description='Importe alzette.so dans le fichier Python')
        self.parse_arguments()

    def parse_arguments(self):
        self.parser.add_argument('-h', '--help', action='help', help="Affiche ce message d'aide")
        self.parser.add_argument('-a', '--alzette', action='store_true', help="Lance Alzette")

        self.args = self.parser.parse_args()

if __name__=="__main__":
    parseur = Parseur()
    if parseur.args.alzette:
        Alzette(0xb7e15162, 0x9e3779b9, 0x6e3449b3)
