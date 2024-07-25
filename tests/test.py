import os
import ctypes
from hypothesis import given
from hypothesis.strategies import integers
from pathlib import Path
import binding
import numpy as np

from reference import alzette, crax

class Tests:

    def __init__(self):
        #self.progs = ["alzette", "crax", "esch", "sparkle"]
        self.functions_names = ["esch", "alzette"]
        self.libraries = {}
        self.functions = {}

        self.load_so()
        self.load_funcs()

        self.tests_passed = 0
        self.total_tests = 0 

        self.test_alzette()

        self.render_results()

    def load_so(self):
        self.library = binding.Wrapper(False).get_library()

    def load_funcs(self):
        for func in self.functions_names:
            self.load_func(func)

    def load_func(self, func):
        try:
            self.functions[func] = binding.Wrapper(False).get_func(func + "_export")
            print(f"function {func} successfully imported")
        except:
            print(f"Couldn't import {func} function")
            exit()

    def run_all_tests(self):
        for func in self.functions_name:
                test(func)

    def process_test_result(self, reference_result, jasmin_result):
        if reference_result[0] == jasmin_result[0] and reference_result[1] == jasmin_result[1]: # A réécrire
            self.tests_passed +=1
        self.total_tests +=1

    def render_results(self):
        try:
            pourcent = (self.tests_passed/self.total_tests)*100
            print(f"Tests passed: {pourcent}% ({self.tests_passed}/{self.total_tests}) ")
        except:
            print(f"Tests passed: 0% ({self.tests_passed}/{self.total_tests}) ")


    @given(integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647))
    def test_alzette(self, c, x, y):
        alzette_instance = alzette.Alzette_t()
        
        reference_res = alzette_instance.alzette(c, x, y)
        jasmin_res = self.functions["alzette"](c, x, y)

        return_y = ctypes.c_uint32(jasmin_res& 0xFFFFFFFF)
        return_x = ctypes.c_uint32((jasmin_res >> 32) & 0xFFFFFFFF)

        self.process_test_result(reference_res, (return_x, return_y))

if __name__=="__main__":
    test = Tests()
