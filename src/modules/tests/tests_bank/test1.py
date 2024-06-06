import modules.alzettepython.alzettepython as AlzettePython 
import modules.alzettejasmin.alzettejasmin as AlzetteJasmin 

from tabulate import tabulate

class test:
    def __init__(self, values, additional_data = None):
        self.values = values
        self.additionnal_data = additional_data

        self.results = [[], []]

        self.run_test()

        self.rendered_results = self.render_results()

    def run_test(self):
        self.set_header(["variable", "python", "jasmin", "test"])
        self.run_python_implementation()
        self.run_jasmin_implementation()
        self.add_results(["x", self.result_x_python, self.result_x_jasmin, self.result_x_python==self.result_x_jasmin])
        self.add_results(["y", self.result_y_python, self.result_y_jasmin, self.result_y_python==self.result_y_jasmin])
        pass #run test function

    def run_python_implementation(self, values = None):
        if values == None:
            alzettePython = AlzettePython.AlzettePython_t(self.values)
        else:
            alzettePython = AlzettePython.AlzettePython_t(self.values)
        self.result_x_python, self.result_y_python = alzettePython.alzette()

    def run_jasmin_implementation(self, values = None):
        if values == None:
            alzetteJasmin = AlzetteJasmin.AlzetteJasmin_t(self.values)
        else:
            alzetteJasmin = AlzetteJasmin.AlzetteJasmin_t(values)
        self.result_x_jasmin, self.result_y_jasmin = alzetteJasmin.alzette()

    def set_header(self, header):
        self.results[1] = header

    def add_results(self, results):
        self.results[0].append(results)

    def render_results(self):
        return tabulate(self.results[0], self.results[1], tablefmt="grid")

    def __repr__(self):
        return self.rendered_results
