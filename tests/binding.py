import sys
import argparse
import ctypes
import os
import subprocess
from pathlib import Path

from tabulate import tabulate

from hypothesis import given
from hypothesis.strategies import text 

class Parseur:
    def __init__(self):
        self.parser = argparse.ArgumentParser(usage='python3 alzette.py [OPTIONS]', add_help=False, description='Python script to launch a Jasmins\' implementation of Alzette')
        self.parse_arguments()

    def parse_arguments(self):
        self.parser.add_argument('-h', '--help', action='help', help="shows this help message")
        self.parser.add_argument('-p', '--program', type=str, help='functions to summon. Choices: crax_export, esch_export, schwaemm_export, sparkle384_11_export, sparkle384_7_export')
        self.parser.add_argument('-c', '--constant', help="Alzette required argument #1")
        self.parser.add_argument('-xa', '--axword', help="Alzette required argument #2")
        self.parser.add_argument('-ya', '--ayword', help="Alzette required argument #3")
        self.parser.add_argument('-xc', '--cxword', help="Crax required argument #1")
        self.parser.add_argument('-yc', '--cyword', help="Crax required argument #2")
        self.parser.add_argument('-k0', '--key_0', help="Crax required argument #3")
        self.parser.add_argument('-k1', '--key_1', help="Crax required argument #4")
        self.parser.add_argument('-k2', '--key_2', help="Crax required argument #5")
        self.parser.add_argument('-k3', '--key_3', help="Crax required argument #6")
        self.parser.add_argument('-e', '--esch_entry', help="Esch: Text to be hashed")
        self.parser.add_argument('-x0', '--sparkle_x0', help="x_0 value for Sparkle")
        self.parser.add_argument('-y0', '--sparkle_y0', help="y_0 value for Sparkle")
        self.parser.add_argument('-x1', '--sparkle_x1', help="x_1 value for Sparkle")
        self.parser.add_argument('-y1', '--sparkle_y1', help="y_1 value for Sparkle")
        self.parser.add_argument('-x2', '--sparkle_x2', help="x_2 value for Sparkle")
        self.parser.add_argument('-y2', '--sparkle_y2', help="y_2 value for Sparkle")
        self.parser.add_argument('-x3', '--sparkle_x3', help="x_3 value for Sparkle")
        self.parser.add_argument('-y3', '--sparkle_y3', help="y_3 value for Sparkle")
        self.parser.add_argument('-x4', '--sparkle_x4', help="x_4 value for Sparkle")
        self.parser.add_argument('-y4', '--sparkle_y4', help="y_4 value for Sparkle")
        self.parser.add_argument('-x5', '--sparkle_x5', help="x_5 value for Sparkle")
        self.parser.add_argument('-y5', '--sparkle_y5', help="y_5 value for Sparkle")

        self.args = self.parser.parse_args()

class Wrapper:

	def __init__(self):
		self.int32 = ctypes.c_int32
		self.int64 = ctypes.c_int64

		self.args = {"alzette_export": [self.int32, self.int32, self.int32],"crax_export": [self.int32, self.int32, self.int32, self.int32, self.int32, self.int32], "esch_export" : [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char)], "sparkle384_7_export": [ctypes.c_int32 * 12], "sparkle384_11_export": [ctypes.c_int32 * 12]}

		self.required_flags = {"alzette_export": ["constant", "axword", "ayword"], "crax_export": ["cxword","cyword","key_0","key_1","key_2","key_3"], "esch_export": ["esch_entry"], "sparkle384_7": ["state_pointer"], "sparkle384_11_export": ['sparkle_x0', 'sparkle_x1', 'sparkle_x2', 'sparkle_x3', 'sparkle_x4', 'sparkle_y0', 'sparkle_y1', 'sparkle_y2', 'sparkle_y3', 'sparkle_y4'], "sparkle384_7_export": ['sparkle_x0', 'sparkle_x1', 'sparkle_x2', 'sparkle_x3', 'sparkle_x4', 'sparkle_y0', 'sparkle_y1', 'sparkle_y2', 'sparkle_y3', 'sparkle_y4']} 


		self.loadlibraries()

		# "schwaemm_export" : [self.int64, int256, self.int64, self.int64, self.int64], -> pas de u256 dans ctypes? 

		self.parseur = Parseur()
		self.parseur.args.program = self.parseur.args.program + "_export"
		self.set_func(self.parseur.args.program)

	def loadlibraries(self):
		self.try_load_library()

	def try_load_library(self):
		if Path(f"../shared/sparkle_suite.so").exists():
			self.load_library()
			return
		else:
			sys.stdout.write(f"Jasmin sparkle suite library (.so) not found. Please compile it.\nExiting\n")
			exit()

	def load_library(self):
		self.library = ctypes.cdll.LoadLibrary("../shared/sparkle_suite.so")

	def set_func(self, function):
		self.check_args()
		func = getattr(self.library, function)
		func.argtypes = self.args[function]
		match function:
			case "alzette_export":
				alzette_res = func(self.int32(int(self.parseur.args.constant)), self.int32(int(self.parseur.args.axword)), self.int32(int(self.parseur.args.ayword)))
				print(f"Alzette ran with:\n\tc: {self.parseur.args.constant}\n\tx: {self.parseur.args.axword}\n\ty: {self.parseur.args.ayword}\n\nOutput: {alzette_res}")
			case "crax_export":
				crax_res_64 = func(self.int32(int(self.parseur.args.cxword)), self.int32(int(self.parseur.args.cyword)), self.int32(int(self.parseur.args.key_0)),self.int32(int(self.parseur.args.key_1)),self.int32(int(self.parseur.args.key_2)),self.int32(int(self.parseur.args.key_3)))
				crax_res_x = crax_res_64 & 0xFFFFFFFF
				crax_res_y = (crax_res_64 >> 32) & 0xFFFFFFFF
				print(f"Crax ran with:\n\tx: {self.parseur.args.cxword}\n\ty: {self.parseur.args.cyword}\n\tkey_0: {self.parseur.args.key_0}\n\tkey_1: {self.parseur.args.key_1}\n\tkey_2: {self.parseur.args.key_2}\n\tkey_3: {self.parseur.args.key_3}\n\nOutput:\n\tx: {crax_res_x}\n\ty: {crax_res_y}")
			case "esch_export":
				output_str = (ctypes.c_ubyte * 32)()
				buffer = ctypes.create_string_buffer(self.parseur.args.esch_entry.encode('utf-8'))

				start_ptr = ctypes.addressof(buffer) 
				end_ptr = start_ptr + len(self.parseur.args.esch_entry)

				func(ctypes.cast(start_ptr, ctypes.POINTER(ctypes.c_char)), ctypes.cast(end_ptr, ctypes.POINTER(ctypes.c_char)), ctypes.cast(output_str, ctypes.POINTER(ctypes.c_char)))
				esch_output = ""
				for i in range(32):
					esch_output += (str(hex(output_str[i]))[2:])
				print(f"Esch ran with\n\t{self.parseur.args.esch_entry}\nOutput:\n\t{esch_output}")

			case "sparkle384_7_export":
				ints = ctypes.c_int32 * 12
				sparkle_args = ints(int(self.parseur.args.sparkle_x0), int(self.parseur.args.sparkle_x1), int(self.parseur.args.sparkle_x2), int(self.parseur.args.sparkle_x3), int(self.parseur.args.sparkle_x4), int(self.parseur.args.sparkle_y0), int(self.parseur.args.sparkle_y1), int(self.parseur.args.sparkle_y2), int(self.parseur.args.sparkle_y3), int(self.parseur.args.sparkle_y4), int(self.parseur.args.sparkle_x5), int(self.parseur.args.sparkle_y5))
				func(sparkle_args)
				sparkle_output = f"Sparkle384_7 ran. Output:\n\t"
				for i in range(12):
					sparkle_output += ["x","y"][i%2] + f"{i//2} : " + str(sparkle_args[i]) + "\n\t"
				print(sparkle_output)

			case "sparkle384_11_export":
				ints = ctypes.c_int32 * 12
				sparkle_args = ints(int(self.parseur.args.sparkle_x0), int(self.parseur.args.sparkle_x1), int(self.parseur.args.sparkle_x2), int(self.parseur.args.sparkle_x3), int(self.parseur.args.sparkle_x4), int(self.parseur.args.sparkle_y0), int(self.parseur.args.sparkle_y1), int(self.parseur.args.sparkle_y2), int(self.parseur.args.sparkle_y3), int(self.parseur.args.sparkle_y4), int(self.parseur.args.sparkle_x5), int(self.parseur.args.sparkle_y5))
				func(sparkle_args)
				sparkle_output = f"Sparkle384_11 ran. Output:\n\t"
				for i in range(12):
					sparkle_output += ["x","y"][i%2] + f"{i//2} : " + str(sparkle_args[i]) + "\n\t"
				print(sparkle_output)

	def check_args(self):
		if self.parseur.args.program:
			valid = 1
			missings=[]
			for flag in self.required_flags[self.parseur.args.program]:
				if flag not in self.parseur.args:
					if self.parseur.args.flag == None:
						valid = 0
						missings.append(flag)
		if valid:
			pass
		else:
			print(f"Error: missing {" ".join(missings)} flag{['','s'][len(missings) >1]}")
			exit()


if __name__ == "__main__":
	wrapper = Wrapper()
