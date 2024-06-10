import modules.alzettepython.alzettepython as AlzettePython 
import modules.alzettejasmin.alzettejasmin as AlzetteJasmin 
from hypothesis import given
from hypothesis.strategies import integers

@given(integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647))
def test(test_manager, c, x, y):
    #print(f"{x}, {y}, {c}")
    python_instance = AlzettePython.AlzettePython_t()
    jasmin_instance = AlzetteJasmin.AlzetteJasmin_t()

    python_return_x, python_return_y = python_instance.alzette(c, x, y)
    jasmin_return_x, jasmin_return_y = jasmin_instance.alzette(c, x, y)

    test = ((python_return_x, python_return_y) == (jasmin_return_x, jasmin_return_y))

    if test:
        test_manager.add_success()
    else:
        test_manager.add_failure()

    print(f"[{['\033[0;31m-\033[0;37m','\033[0;32m+\033[0;37m'][test]}] test {['\033[0;31mfailed\033[0;37m\t','\033[0;32msucceeded\033[0;37m'][test]}\t : c: {c}, x: {x}, y: {y}\t\n\tJasmin returns: (x: {['\033[0;31m' + str(jasmin_return_x) +'\033[0;37m','\033[0;32m' + str(jasmin_return_x) + '\033[0;37m'][jasmin_return_x == python_return_x]} y: {['\033[0;31m' + str(jasmin_return_y) + '\033[0;37m','\033[0;32m' + str(jasmin_return_y) + '\033[0;37m'][jasmin_return_y == python_return_y]})\n\tPython returns: (x: {['\033[0;31m' + str(python_return_x) + '\033[0;37m','\033[0;32m' + str(python_return_x) + '\033[0;37m'][python_return_x == jasmin_return_x]} y: {['\033[0;31m' + str(python_return_y) + '\033[0;37m','\033[0;32m' + str(python_return_y) + '\033[0;37m'][python_return_y == jasmin_return_y]})\n")
