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

    def init_structs(self, string):

        output_ptr = (ctypes.c_ubyte * 32)() 

        buffer = ctypes.create_string_buffer(string.encode('utf-8'))

        start_ptr = ctypes.addressof(buffer)
        end_ptr = start_ptr + len(string.encode('utf-8'))

        end_ptr = ctypes.cast(end_ptr, ctypes.POINTER(ctypes.c_char))
        start_ptr = ctypes.cast(start_ptr, ctypes.POINTER(ctypes.c_char))
        output_ptr = ctypes.cast(output_ptr, ctypes.POINTER(ctypes.c_char))

        return (start_ptr, end_ptr, output_ptr)
    
    @given(text())
    def esch(self, string):
        jasmin_result = ""
        reference_result = ""

        reference_result += self.format_output_text(self.esch_reference(string))

        output = self.esch_jasmin(string)

        jasmin_result += self.format_output_text(self.esch_reference(string))

        condition = (jasmin_result == reference_result)
        jasmin_result = self.format_result_text(jasmin_result, condition)
        reference_result = self.format_result_text(reference_result, condition)

        self.process_test_results((jasmin_result, reference_result))

    def esch_jasmin(self, string):

        (start_ptr, end_ptr, output_ptr) = self.init_structs(string)

        self.jasmin_esch_dll.esch(start_ptr, end_ptr, output_ptr)

        return output_ptr

    def esch_reference(self, string):

        (start_ptr, end_ptr, output_ptr) = self.init_structs(string)

        self.reference_esch_dll.esch(start_ptr, end_ptr, output_ptr)

        return output_ptr

    def test_esch_reference(self, string):
        output = self.esch_reference(string)

        for i in range(32):
            if output[i]:
                sys.stdout.write(f"{hex(output[i])[2:]}")

    def test_esch_jasmin(self, string):
        output = self.esch_jasmin(string)
        
        return self.format_output_text(output)

    def compare_esch(self, string):
        result = {"Jasmin" : [], "Reference" : []}

        jasmin_result = []
        reference_result = []

        output = self.esch_reference(string)
        for i in range(32):
            reference_result.append((hex(output[i])))

        output = self.esch_jasmin(string)
        for i in range(32):
            jasmin_result.append(str(hex(output[i])))

        for i in range(min(len(jasmin_result), len(reference_result))):
            condition = (jasmin_result[i] == reference_result[i])
            
            jasmin_result[i] = self.format_result_text(jasmin_result[i], condition)
            reference_result[i] = self.format_result_text(reference_result[i], condition)

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
        self.results["Result"].append(self.format_result_text(["Failed", "Passed"], (tuple[0] == tuple[1])))

    def format_result_text(self, value, condition):
        if isinstance(value, str):
            if condition:
                return f"\033[0;32m{value}\033[0m"
            else:
                return f"\033[0;31m{value}\033[0m"
        else:
            if not condition:
                return f"\033[0;31m{value[0]}\033[0m"
            else:
                return f"\033[0;32m{value[1]}\033[0m"

    def format_output_text(self, output_ptr):
        output = "0x"
        for i in range(32):
            output += (f"{output_ptr[i].hex()}")

        return output

if __name__ == "__main__":
    eschInstance = Esch_t()

    eschInstance.test_full_esch(1)
