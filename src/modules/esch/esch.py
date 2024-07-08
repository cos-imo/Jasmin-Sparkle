import sys
import ctypes
import os
import subprocess
from pathlib import Path

from tabulate import tabulate

from hypothesis import given
from hypothesis.strategies import integers

class Esch_t:

    def __init__(self):

        self.try_load_esch_library()
        self.try_load_esch_reference_library()

    def try_load_esch_library(self):
        if Path("esch.so").exists():
            self.load_esch_library()
            return
        else:
            sys.stdout.write("Jasmin Esch library (.so) not found. Please compile it.\nExiting\n")
            exit()

    def load_esch_library(self):
        try:
            self.jasmin_esch_dll = ctypes.cdll.LoadLibrary("esch.so")

            args = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char)]

            self.jasmin_esch_dll.esch.argtypes = args
            self.jasmin_esch_dll.esch.restype = None

        except:
            sys.stdout.write("Couldn't import esch_jasmin.so library\nExiting\n")
            exit()

    def try_load_esch_reference_library(self):
        if Path("esch_reference.so").exists():
            self.load_esch_reference_library()
            return
        else:
            sys.stdout.write("C esch library (.so) not found. Please compile it.\nExiting\n")
            exit()

    def load_esch_reference_library(self):
        try:
            self.reference_esch_dll = ctypes.cdll.LoadLibrary("esch_reference.so")

            args = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char)]

            self.reference_esch_dll.esch.argtypes = args
            self.reference_esch_dll.esch.restype = None

        except:
            sys.stdout.write("Couldn't import esch_reference.so library\nExiting\n")
            exit()


    def esch(self, x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5):
        #given ...

        self.ints = ctypes.c_int32 *12 
        args = [ctypes.c_int32 * 12]

        array_jasmin = self.ints(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)
        array_reference = self.ints(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)

        print("Given values:")

        print(f"x_0 : {array_jasmin[0]}        y_0 : {array_jasmin[1]}\nx_1 : {array_jasmin[2]}        y_1 : {array_jasmin[3]} \nx_2 : {array_jasmin[4]}        y_2 : {array_jasmin[5]}\nx_3 : {array_jasmin[6]}        y_3 : {array_jasmin[7]}\nx_4 : {array_jasmin[8]}        y_0 : {array_jasmin[9]}\nx_5 : {array_jasmin[10]}        y_5 : {array_jasmin[11]}" )

        self.jasmin_esch_dll.esch(array_jasmin)

        print("JASMIN")

        print(f"x_0 : {array_jasmin[0]}        y_0 : {array_jasmin[1]}\nx_1 : {array_jasmin[2]}        y_1 : {array_jasmin[3]} \nx_2 : {array_jasmin[4]}        y_2 : {array_jasmin[5]}\nx_3 : {array_jasmin[6]}        y_3 : {array_jasmin[7]}\nx_4 : {array_jasmin[8]}        y_0 : {array_jasmin[9]}\nx_5 : {array_jasmin[10]}        y_5 : {array_jasmin[11]}" )

        print(array_reference == array_jasmin)

        self.reference_esch_dll.esch(array_reference, ctypes.c_uint32(6), ctypes.c_uint32(0))

        print("Reference")

        print(f"x_0 : {array_reference[0]}        y_0 : {array_reference[1]}\nx_1 : {array_reference[2]}        y_1 : {array_reference[3]}\n x_2 : {array_reference[4]}        y_2 : {array_reference[5]}\nx_3 : {array_reference[6]}        y_3 : {array_reference[7]}\nx_4 : {array_reference[8]}        y_0 : {array_reference[9]}\nx_5 : {array_reference[10]}        y_5 : {array_reference[11]}" )

        test = (array_jasmin == array_reference)

        print(f"{test}\n\n")

    def esch_jasmin(self, start_ptr, end_ptr, output_ptr):

        self.jasmin_esch_dll.esch(start_ptr, end_ptr, output_ptr)

        return output_ptr 

    def esch_reference(self, start_ptr, end_ptr, output_ptr):

        self.reference_esch_dll.esch(start_ptr, end_ptr, output_ptr)

        return output_ptr 

    def test_esch_reference(self, string):
        output_str = (ctypes.c_ubyte * 32)() 

        buffer = ctypes.create_string_buffer(string.encode('utf-8'))

        start_pointer = ctypes.addressof(buffer)
        end_pointer = start_pointer + len(string.encode('utf-8'))

        self.esch_reference(buffer, ctypes.cast(end_pointer, ctypes.POINTER(ctypes.c_char)), ctypes.cast(output_str, ctypes.POINTER(ctypes.c_char)))
        for i in range(32):
            if output_str[i]:
                sys.stdout.write(f"{hex(output_str[i])[2:]}")

    def test_esch_jasmin(self, string):
        output_str = (ctypes.c_ubyte * 32)() 

        buffer = ctypes.create_string_buffer(string.encode('utf-8'))

        start_pointer = ctypes.addressof(buffer)
        end_pointer = start_pointer + len(string.encode('utf-8')) - 1

        self.esch_jasmin(ctypes.cast(buffer, ctypes.POINTER(ctypes.c_char)), ctypes.cast(end_pointer, ctypes.POINTER(ctypes.c_char)), ctypes.cast(output_str, ctypes.POINTER(ctypes.c_char)))
        for i in range(32):
            sys.stdout.write(f"{hex(output_str[i])}\t")

    def compare_esch(self, string):
        result = {"Jasmin" : [], "Reference" : []}

        jasmin_result = []
        reference_result = []

        output_str = (ctypes.c_ubyte * 32)() 

        buffer = ctypes.create_string_buffer(string.encode('utf-8'))

        start_pointer = ctypes.addressof(buffer)
        end_pointer = start_pointer + len(string.encode('utf-8'))

        self.esch_reference(ctypes.cast(buffer, ctypes.POINTER(ctypes.c_char)), ctypes.cast(end_pointer, ctypes.POINTER(ctypes.c_char)), ctypes.cast(output_str, ctypes.POINTER(ctypes.c_char)))
        for i in range(32):
            reference_result.append(str(hex(output_str[i])))

        output_str = (ctypes.c_ubyte * 32)() 
        self.esch_jasmin(ctypes.cast(start_pointer, ctypes.POINTER(ctypes.c_char)), ctypes.cast(end_pointer, ctypes.POINTER(ctypes.c_char)), ctypes.cast(output_str, ctypes.POINTER(ctypes.c_char)))
        for i in range(32):
            jasmin_result.append(str(hex(output_str[i])))

        for i in range(min(len(jasmin_result), len(reference_result))):
            if jasmin_result[i] == reference_result[i]:
                jasmin_result[i] = f"\033[0;32m{jasmin_result[i]}\033[0m"
                reference_result[i] = f"\033[0;32m{reference_result[i]}\033[0m"
            elif jasmin_result[i] in reference_result:
                jasmin_result[i] = f"\033[0;33m{jasmin_result[i]}\033[0m"
                if reference_result[i] in jasmin_result:
                    reference_result[i] = f"\033[0;33m{reference_result[i]}\033[0m"
                else:
                    reference_result[i] = f"\033[0;31m{reference_result[i]}\033[0m"
            else:
                jasmin_result[i] = f"\033[0;31m{jasmin_result[i]}\033[0m"
                reference_result[i] = f"\033[0;31m{reference_result[i]}\033[0m"

        result["Jasmin"] = jasmin_result
        result["Reference"] = reference_result

        print(tabulate(result, headers="keys"))

if __name__ == "__main__":
    eschInstance = Esch_t()

    string = "1234567890123U456" # Note: Segmentation fault on esch official implementation when called with an empty string?? 
    
    eschInstance.compare_esch(string)
