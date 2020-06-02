from __future__ import print_function
from libc cimport stdlib

def fib(n):
    """Print the Fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b

    print()

cpdef parse_charptr_to_py_int(char* s):
    assert s is not NULL, "byte string value is NULL"
    stdlib.atoi(s)
