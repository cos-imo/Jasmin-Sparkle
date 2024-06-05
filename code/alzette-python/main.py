from alzettepython import Alzette as Alzette 
import argparse

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
        Alzette(parseur, parseur.args.python_alzette[0], parseur.args.python_alzette[1], parseur.args.python_alzette[2])
    elif parseur.args.jasmin_alzette:
        Alzette(parseur, parseur.args.jasmin_alzette[0], parseur.args.jasmin_alzette[1], parseur.args.jasmin_alzette[2])
