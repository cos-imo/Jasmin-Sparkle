from tabulate import tabulate
import modules.tests.tests_bank.test1

class testmanager_t:
    def __init__(self, choice="all", python_implementation = None, jasmin_implementation = None, values = [1,2,3]):
        self.test_library = [modules.tests.tests_bank.test1]

        self.python_implementation = python_implementation
        self.jasmin_implementation = jasmin_implementation

        self.values = values

        self.successes = 0
        self.failures = 0

        self.results = []
        self.headers = ["c_value", "x_value", "y_value", "status"]

        self.run_test()
        self.render_results()


    def set_python_implementation(self, python_implementation):
        self.python_implementation = python_implementation

    def set_jasmin_implementation(self, jasmin_implementation):
        self.jasmin_implementation = jasmin_implementation

    def run_test(self, test="all"):
        if test == "all":
            for i in range(len(self.test_library)):
                test_data = self.test_library[i].test(self)
                #self.results.append(test_data)
            return
        else:
            test_result = self.test_library[test].test(self.values)
            print("test don")
            print(test_result)

    def render_results(self):
        print(f"Ran {self.successes + self.failures} tests.")
        print(f"\tSuccesse rate : {(self.successes/(self.successes + self.failures))*100} % ({self.successes}/{self.successes + self.failures})\n\tFailure rate : {(self.failures/(self.successes + self.failures))*100}% ({self.failures}/{self.failures + self.successes})\n")

    def add_success(self):
        self.successes += 1 

    def add_failure(self):
        self.failures += 1
