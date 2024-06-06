import modules
import argparse
from pathlib import Path

class Parseur:
    def __init__(self):
        self.parser = argparse.ArgumentParser(usage='python3 alzette.py [OPTIONS]', add_help=False, description='Python script to launch a Jasmins\' implementation of Alzette')
        self.parse_arguments()

    def check_test(self, option):
        try:
            int(option)
            if Path("modules/tests/tests_bank/test" + option + ".py").exists():
                return
            else:
                raise argparse.ArgumentTypeError("Error: your test hasn't been found.\n\tPlease make sure to use 'all' to run all tests or X where X is an integer corresponding to the associated test file in \n\tmodules/tests/tests_bank/testX.py\n\n")
        except ValueError:
            pass
        if option == "all":
            return option 
        raise argparse.ArgumentTypeError("Error: your test hasn't been found.\n\tPlease make sure to use 'all' to run all tests or X where X is an integer corresponding to the associated test file in \n\tmodules/tests/tests_bank/testX.py\n\n")

    def parse_arguments(self):
        self.parser.add_argument('-h', '--help', action='help', help="shows this help message")
        self.parser.add_argument('x', default = "0x67425301", type=int, help='Value for x')
        self.parser.add_argument('y', default = "0xEDFCBA45", type=int, help='Value for y')
        self.parser.add_argument('c', default = "0x98CBADFE", type=int, help='Value for c')
        self.parser.add_argument('-p', '--python_alzette', action='store_true', help="Launches Alzette (Python implementation)")
        self.parser.add_argument('-j', '--jasmin_alzette', action='store_true', help="Launches Alzette (Jasmin implementation)")
        self.parser.add_argument('-t', '--test', type = self.check_test, help="Launches tests")
        self.parser.add_argument('-d', '--display', action='store_true', help="Display mode: displays results")

        self.args = self.parser.parse_args()

if __name__=="__main__":
    parseur = Parseur()

    values = [parseur.args.c, parseur.args.x, parseur.args.y]
    
    argumentparser = modules.core.CoreLauncher(parseur, values)
