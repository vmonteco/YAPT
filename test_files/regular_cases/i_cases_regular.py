# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    [b'%i\n', ctypes.c_int(0)],
    [b'% i\n', ctypes.c_int(0)],
    [b'%+i\n', ctypes.c_int(0)],
    [b'%-i\n', ctypes.c_int(0)],
    [b'%0i\n', ctypes.c_int(0)],
    [b'%#i\n', ctypes.c_int(0)],
    [b'%10i\n', ctypes.c_int(0)],
    [b'%.6i\n', ctypes.c_int(0)],
    [b'%hhi\n', ctypes.c_int(0)],
    [b'%lli\n', ctypes.c_int(0)],
    [b'%hi\n', ctypes.c_int(0)],
    [b'%li\n', ctypes.c_int(0)],
    [b'%ji\n', ctypes.c_int(0)],
    [b'%zi\n', ctypes.c_int(0)],
]


mixed_cases = [
    [b'% 0+-#10.5lli', ctypes.c_int(42)],
    [b'%-010zi\\n', ctypes.c_short(0)],
]

test_sets = [
    {
        'name': 'i tests - basics.',
        'cases': basic_cases
    },
    {
        'name': 'i tests - basics.',
        'cases': mixed_cases
    }
]

cases_generator = generator_factory(test_sets)
