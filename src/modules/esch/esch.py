import sys
import ctypes
import os
import subprocess
from pathlib import Path

from tabulate import tabulate

from hypothesis import given
from hypothesis.strategies import text 

class Esch_t:

    def __init__(self):

        self.try_load_esch_library()
        self.try_load_esch_reference_library()

        self.results = {"Jasmin": [], "Reference":[], "Result":[]}

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
    
    @given(text())
    def esch(self, string):
        jasmin_result = ""
        reference_result = ""

        output_str = (ctypes.c_ubyte * 32)() 

        buffer = ctypes.create_string_buffer(string.encode('utf-8'))

        start_pointer = ctypes.addressof(buffer)
        end_pointer = start_pointer + len(string.encode('utf-8'))

        self.esch_reference(ctypes.cast(buffer, ctypes.POINTER(ctypes.c_char)), ctypes.cast(end_pointer, ctypes.POINTER(ctypes.c_char)), ctypes.cast(output_str, ctypes.POINTER(ctypes.c_char)))
        for i in range(32):
            reference_result += (str(hex(output_str[i]))[2:])

        output_str = (ctypes.c_ubyte * 32)() 
        self.esch_jasmin(ctypes.cast(start_pointer, ctypes.POINTER(ctypes.c_char)), ctypes.cast(end_pointer, ctypes.POINTER(ctypes.c_char)), ctypes.cast(output_str, ctypes.POINTER(ctypes.c_char)))
        for i in range(32):
            jasmin_result += (str(hex(output_str[i]))[2:])

        if jasmin_result == reference_result:
            jasmin_result = f"\033[0;32m{jasmin_result}\033[0m"
            reference_result = f"\033[0;32m{reference_result}\033[0m"
        else:
            jasmin_result = f"\033[0;31m{jasmin_result}\033[0m"
            reference_result = f"\033[0;31m{reference_result}\033[0m"

        self.process_test_results((jasmin_result, reference_result))

    def esch_jasmin(self, start_ptr, end_ptr, output_ptr):

        self.jasmin_esch_dll.esch(start_ptr, end_ptr, output_ptr)

    def esch_reference(self, start_ptr, end_ptr, output_ptr):

        self.reference_esch_dll.esch(start_ptr, end_ptr, output_ptr)

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

    def test_full_esch(self, ntests):
        for i in range(ntests):
            self.esch()

        print(tabulate(self.results, headers="keys", tablefmt='grid'))
        print(f"test passed: {self.results['Result'].count(True)}/{ntests*100} ({(self.results['Result'].count("\033[0;32mPassed\033[0m"))/(ntests)}%)")
        print("done")

    def process_test_results(self, tuple):
        self.results["Jasmin"].append(tuple[0])
        self.results["Reference"].append(tuple[1])
        self.results["Result"].append(["\033[0;31mFailed\033[0m", "\033[0;32mPassed\033[0m"][tuple[0] == tuple[1]])

if __name__ == "__main__":
    eschInstance = Esch_t()

    eschInstance.test_full_esch(1)
