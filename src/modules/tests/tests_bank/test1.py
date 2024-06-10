import modules.alzettepython.alzettepython as AlzettePython 
import modules.alzettejasmin.alzettejasmin as AlzetteJasmin 
from hypothesis import given
from hypothesis.strategies import integers

@given(integers(min_value = 0, max_value=9999), integers(min_value=0, max_value = 9999), integers(min_value = 0, max_value = 9999))
def test(c, x, y):
    print(f"{x}, {y}, {c}")
    assert AlzettePython.AlzettePython_t([c, x, y]) == AlzetteJasmin.AlzetteJasmin_t([c, x, y])
