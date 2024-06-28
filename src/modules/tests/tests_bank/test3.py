import modules
import sparklereference.sparklereference as sparklereference 
import sparklejasmin as jazzsparkle 
from hypothesis import given
from hypothesis.strategies import integers

@given(integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647), integers(min_value = -2147483647, max_value = 2147483647))
def test(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5):
    reference_instance = sparklereference.()
    jasmin_instance = jazzsparkle.SparkleJasmin_t()

    python_return_x_0, python_return_y_0, python_return_x_1, python_return_y_1, python_return_x_2, python_return_y_2, python_return_x_3, python_return_y_3, python_return_x_4, python_return_y_4, python_return_x_5, python_return_y_5 = reference_instance.crax(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)
    jasmin_return_x_0, jasmin_return_y_0, jasmin_return_x_1, jasmin_return_y_1, jasmin_return_x_2, jasmin_return_y_2, jasmin_return_x_3, jasmin_return_y_3, jasmin_return_x_4, jasmin_return_y_4, jasmin_return_x_5, jasmin_return_y_5 = jasmin_instance.sparkle(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)

    test = ((python_return_x, python_return_y) == (jasmin_return_x, jasmin_return_y))

    if test:
        test_manager.add_success()
    else:
        test_manager.add_failure()

    print(f"[{['\033[0;31m-\033[0;37m','\033[0;32m+\033[0;37m'][test]}] CRAX test {['\033[0;31mfailed\033[0;37m\t','\033[0;32msucceeded\033[0;37m'][test]}\t : key: [{key_0}, {key_1}, {key_2}, {key_3}], x: {x}, y: {y}\t\n\tJasmin returns: (x: {['\033[0;31m' + str(jasmin_return_x) +'\033[0;37m','\033[0;32m' + str(jasmin_return_x) + '\033[0;37m'][jasmin_return_x == python_return_x]}, y: {['\033[0;31m' + str(jasmin_return_y) + '\033[0;37m','\033[0;32m' + str(jasmin_return_y) + '\033[0;37m'][jasmin_return_y == python_return_y]})\n\tPython returns: (x: {['\033[0;31m' + str(python_return_x) + '\033[0;37m','\033[0;32m' + str(python_return_x) + '\033[0;37m'][python_return_x == jasmin_return_x]}, y: {['\033[0;31m' + str(python_return_y) + '\033[0;37m','\033[0;32m' + str(python_return_y) + '\033[0;37m'][python_return_y == jasmin_return_y]})\n")


if __name__=="__main__":
    test()
