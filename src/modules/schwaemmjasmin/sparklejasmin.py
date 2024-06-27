import sys
import ctypes
import os
import subprocess
from pathlib import Path

from hypothesis import given
from hypothesis.strategies import integers

class Sparkle_t:

    def __init__(self):

        self.load_jasmin_library()
        self.load_jasmin7_library()
        self.load_jasmin11_library()
        self.load_c_library()

    def load_jasmin_library(self):
        if Path("sparkle_jasmin.so").exists():
            self.try_load_jasmin_library()
            return
        else:
            sys.stdout.write("Jasmin Sparkle library (.so) not found. Please compile it.\nExiting\n")
            exit()

    def try_load_jasmin_library(self):
        try:
            self.jasmin_sparkle_dll = ctypes.cdll.LoadLibrary("sparkle_jasmin.so")

            args = [ctypes.c_uint32 * 12]

            self.jasmin_sparkle_dll.sparkle.argtypes = args
            self.jasmin_sparkle_dll.sparkle.restype = None

        except:
            sys.stdout.write("Couldn't import sparkle_jasmin.so library\nExiting\n")
            exit()


    def load_jasmin7_library(self):
        if Path("sparkle7_jasmin.so").exists():
            self.try_load_jasmin7_library()
            return
        else:
            sys.stdout.write("Jasmin Sparkle7 library (.so) not found. Please compile it.\nExiting\n")
            exit()

    def try_load_jasmin7_library(self):
        try:
            self.jasmin_sparkle7_dll = ctypes.cdll.LoadLibrary("sparkle7_jasmin.so")

            args = [ctypes.c_uint32 * 12]
            print("args defined")

            self.jasmin_sparkle7_dll.sparkle7.argtypes = args
            print("args_done")
            self.jasmin_sparkle7_dll.sparkle384_7.restype = None

        except:
            sys.stdout.write("Couldn't import sparkle7_jasmin.so library\nExiting\n")
            exit()

    def load_jasmin11_library(self):
        if Path("sparkle11_jasmin.so").exists():
            self.try_load_jasmin11_library()
            return
        else:
            sys.stdout.write("Jasmin Sparkle11 library (.so) not found. Please compile it.\nExiting\n")
            exit()

    def try_load_jasmin11_library(self):
        try:
            self.jasmin_sparkle11_dll = ctypes.cdll.LoadLibrary("sparkle11_jasmin.so")

            args = [ctypes.c_uint32 * 12]

            self.jasmin_sparkle11_dll.sparkle384_11.argtypes = args
            self.jasmin_sparkle11_dll.sparkle384_11.restype = None

        except:
            sys.stdout.write("Couldn't import sparkle11_jasmin.so library\nExiting\n")
            exit()

    def load_c_library(self):
        if Path("sparklereference/sparkle.so").exists():
            self.try_load_c_library()
            return
        else:
            sys.stdout.write("C Sparkle library (.so) not found. Please compile it.\nExiting\n")
            exit()

    def try_load_c_library(self):
        try:
            self.reference_sparkle_dll = ctypes.cdll.LoadLibrary("sparklereference/sparkle.so")

            args = [ctypes.c_uint32 * 12, ctypes.c_uint32, ctypes.c_uint32]

            self.reference_sparkle_dll.sparkle.argtypes = args
            self.reference_sparkle_dll.sparkle.restype = None
        except:
            sys.stdout.write("Couldn't import sparkle.so reference library\nExiting\n")
            exit()


    @given(integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647))
    def test_sparkle(self, x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5):

        self.ints = ctypes.c_int32 *12 
        args = [ctypes.c_int32 * 12]

        array_jasmin = self.ints(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)
        array_reference = self.ints(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)

        print("Given values:")

        print(f"x_0 : {array_jasmin[0]}        y_0 : {array_jasmin[1]}\nx_1 : {array_jasmin[2]}        y_1 : {array_jasmin[3]} \nx_2 : {array_jasmin[4]}        y_2 : {array_jasmin[5]}\nx_3 : {array_jasmin[6]}        y_3 : {array_jasmin[7]}\nx_4 : {array_jasmin[8]}        y_0 : {array_jasmin[9]}\nx_5 : {array_jasmin[10]}        y_5 : {array_jasmin[11]}" )

        self.jasmin_sparkle_dll.sparkle(array_jasmin)

        print("JASMIN")

        print(f"x_0 : {array_jasmin[0]}        y_0 : {array_jasmin[1]}\nx_1 : {array_jasmin[2]}        y_1 : {array_jasmin[3]} \nx_2 : {array_jasmin[4]}        y_2 : {array_jasmin[5]}\nx_3 : {array_jasmin[6]}        y_3 : {array_jasmin[7]}\nx_4 : {array_jasmin[8]}        y_0 : {array_jasmin[9]}\nx_5 : {array_jasmin[10]}        y_5 : {array_jasmin[11]}" )

        print(array_reference == array_jasmin)

        self.reference_sparkle_dll.sparkle(array_reference, ctypes.c_uint32(6), ctypes.c_uint32(0))

        print("Reference")

        print(f"x_0 : {array_reference[0]}        y_0 : {array_reference[1]}\nx_1 : {array_reference[2]}        y_1 : {array_reference[3]}\n x_2 : {array_reference[4]}        y_2 : {array_reference[5]}\nx_3 : {array_reference[6]}        y_3 : {array_reference[7]}\nx_4 : {array_reference[8]}        y_0 : {array_reference[9]}\nx_5 : {array_reference[10]}        y_5 : {array_reference[11]}" )

        test = (array_jasmin == array_reference)

        print(f"{test}\n\n")

    def test_sparkle_jasmin(self, x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5):

        self.ints = ctypes.c_uint32 *12 
        array_jasmin = self.ints(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)

        self.jasmin_sparkle_dll.sparkle(array_jasmin)

        return array_jasmin

    def test_sparkle7_jasmin(self, x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5):

        self.ints = ctypes.c_uint32 *12 
        array_jasmin = self.ints(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)

        self.jasmin_sparkle7_dll.sparkle382_7(array_jasmin)

        return array_jasmin

    def test_sparkle11_jasmin(self, x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5):

        self.ints = ctypes.c_uint32 *12 
        array_jasmin = self.ints(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)

        self.jasmin_sparkle11_dll.sparkle384_11(array_jasmin)

        return array_jasmin

    def test_sparkle_reference(self, steps, x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5):

        self.ints = ctypes.c_uint32 *12 
        array_reference = self.ints(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)

        self.reference_sparkle_dll.sparkle(array_reference, ctypes.c_uint32(6), ctypes.c_uint32(steps))

        return array_reference


    def compare_sparkle(self, x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5):
        jasmin_result = self.test_sparkle_jasmin(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)
        reference_result = self.test_sparkle_reference(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)

        print("\n\tJASMIN\t\tREFERENCE")

        for i in range(0,12):
            print(f"{['x','y'][i%2]}_{[int(i/2), int(i/2)][i%2]} : {['\033[0;31m','\033[0;32m'][jasmin_result[i]==reference_result[i]]}{jasmin_result[i]}\t{['\033[0;31m','\033[0;32m'][jasmin_result[i]==reference_result[i]]}{reference_result[i]}\033[0;37m")

        print()


    def compare_sparkle(self, steps, x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5):
        if steps == "export":
            jasmin_result = self.test_sparkle_jasmin(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)
            steps = 11
        elif steps == 7:
            jasmin_result = self.test_sparkle7_jasmin(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)
        elif steps == 11:
            jasmin_result = self.test_sparkle11_jasmin(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)
        reference_result = self.test_sparkle_reference(steps, x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)

        print("\n\tJASMIN\t\tREFERENCE")

        for i in range(0,12):
            print(f"{['x','y'][i%2]}_{[int(i/2), int(i/2)][i%2]} : {['\033[0;31m','\033[0;32m'][jasmin_result[i]==reference_result[i]]}{jasmin_result[i]}\t{['\033[0;31m','\033[0;32m'][jasmin_result[i]==reference_result[i]]}{reference_result[i]}\033[0;37m")

        print()

if __name__ == "__main__":
    SparkleInstance = Sparkle_t()
    for i in range(50):
        SparkleInstance.compare_sparkle(11, 1, 2, 3,4,5,6,7,8,9,10,11,12)
    #SparkleInstance.test_sparkle()
