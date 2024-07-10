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
        reference_raw_result = self.esch_reference(string)
        reference_result = self.format_output_text(reference_raw_result)

        jasmin_raw_result = self.esch_jasmin(string)
        jasmin_result = self.format_output_text(jasmin_raw_result)
        
        self.process_test_results((jasmin_result, reference_result))

    def esch_jasmin(self, string):

        output_ptr = (ctypes.c_ubyte * 32)() 

        buffer = ctypes.create_string_buffer(string.encode('utf-8'))

        start_ptr = ctypes.addressof(buffer)
        end_ptr = start_ptr + len(string.encode('utf-8'))

        self.jasmin_esch_dll.esch(ctypes.cast(start_ptr, ctypes.POINTER(ctypes.c_char)), ctypes.cast(end_ptr, ctypes.POINTER(ctypes.c_char)), ctypes.cast(output_ptr, ctypes.POINTER(ctypes.c_char)))

        return output_ptr

    def esch_reference(self, string):

        output_ptr = (ctypes.c_ubyte * 32)() 

        buffer = ctypes.create_string_buffer(string.encode('utf-8'))

        start_ptr = ctypes.addressof(buffer)
        end_ptr = start_ptr + len(string.encode('utf-8'))

        self.reference_esch_dll.esch(ctypes.cast(start_ptr, ctypes.POINTER(ctypes.c_char)), ctypes.cast(end_ptr, ctypes.POINTER(ctypes.c_char)), ctypes.cast(output_ptr, ctypes.POINTER(ctypes.c_char)))

        return output_ptr

    def test_esch_reference(self, string):
        output = self.esch_reference(string)

        return self.format_output_text(output)

    def test_esch_jasmin(self, string):
        output = self.esch_jasmin(string)
        
        return self.format_output_text(output)

    def compare_esch(self, string):
        result = {"Jasmin" : [], "Reference" : []}

        jasmin_result = []
        reference_result = []

        output = self.esch_reference(string)
        reference_result.append(self.format_output_text(output))

        output = self.esch_jasmin(string)
        jasmin_result.append(self.format_output_text(output))

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
        print(f"test passed: {self.results['Result'].count("\033[0;32mPassed\033[0m")}/{ntests*100} ({(self.results['Result'].count("\033[0;32mPassed\033[0m"))/(ntests)}%)")

    def process_test_results(self, tuple):
        jasmin_result = tuple[0]
        reference_result = tuple[1]

        condition = (jasmin_result == reference_result)
        jasmin_result = self.format_result_text(jasmin_result, condition)
        reference_result = self.format_result_text(reference_result, condition)

        self.results["Jasmin"].append(jasmin_result)
        self.results["Reference"].append(reference_result)
        self.results["Result"].append(self.format_result_text(["Failed", "Passed"], (jasmin_result == reference_result)))

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
            output += (f"{str(hex(output_ptr[i]))[2:]}")

        return output

if __name__ == "__main__":
    eschInstance = Esch_t()

    eschInstance.test_full_esch(1)
