import modules.alzettepython.alzettepython as AlzettePython 
import modules.alzettejasmin.alzettejasmin as AlzetteJasmin 
from hypothesis import given
from hypothesis.strategies import integers

@given(integers(min_value = 0, max_value=9999), integers(min_value=0, max_value = 9999), integers(min_value = 0, max_value = 9999))
def test(c, x, y):
    #print(f"{x}, {y}, {c}")
    python_instance = AlzettePython.AlzettePython_t()
    jasmin_instance = AlzetteJasmin.AlzetteJasmin_t()
    assert (python_instance.alzette(c, x, y) == jasmin_instance.alzette(c, x, y))
