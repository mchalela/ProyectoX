
from proyectox.funciones import fib, prime


class TestFibonacci:

    def test_output_values(self):
        # check exact values
        assert fib(1) == [0, 1, 1]
        assert fib(10) == [0, 1, 1, 2, 3, 5, 8]
        assert fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
        assert fib(50) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_output_type(self):
        # check types
        output = fib(10)
        assert isinstance(output, list)
        assert all([isinstance(n, int) for n in output])


class TestPrimes:

    def test_output_values(self):
        # check exact values
        assert prime(1) == [1]
        assert prime(10) == [1, 2, 3, 5, 7]
        assert prime(20) == [1, 2, 3, 5, 7, 11, 13, 17, 19]
        assert prime(50) == [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 
            29, 31, 37, 41, 43, 47]

    def test_output_type(self):
        # check types
        output = prime(10)
        assert isinstance(output, list)
        assert all([isinstance(n, int) for n in output])