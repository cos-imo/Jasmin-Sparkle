from alzettepython import Alzette as Alzette 
import argparse

class Parseur:
    def __init__(self):
        self.parser = argparse.ArgumentParser(usage='python3 alzette.py [OPTIONS]', add_help=False, description='Python script to launch a Jasmins\' implementation of Alzette')
        self.parse_arguments()

    def parse_arguments(self):
        self.parser.add_argument('-h', '--help', action='help', help="shows this help message")
        self.parser.add_argument('x', type=int, help='Value for x')
        self.parser.add_argument('y', type=int, help='Value for y')
        self.parser.add_argument('c', type=int, help='Value for c')
        self.parser.add_argument('-p', '--python_alzette', action='store_true', help="Launches Alzette (Python implementation)")
        self.parser.add_argument('-j', '--jasmin_alzette', action='store_true', help="Launches Alzette (Jasmin implementation)")
        self.parser.add_argument('-t', '--test', action='store_true', help="Launches tests")
        self.parser.add_argument('-d', '--display', action='store_true', help="Display mode: displays results")

        self.args = self.parser.parse_args()

if __name__=="__main__":
    parseur = Parseur()
    Alzette(parseur, parseur.args.x, parseur.args.y, parseur.args.c)
