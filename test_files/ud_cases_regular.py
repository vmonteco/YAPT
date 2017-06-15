# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    [b'%D\n', ctypes.c_long(0)],
    [b'% D\n', ctypes.c_long(0)],
    [b'%+D\n', ctypes.c_long(0)],
    [b'%-D\n', ctypes.c_long(0)],
    [b'%0D\n', ctypes.c_long(0)],
    [b'%#D\n', ctypes.c_long(0)],
    [b'%10D\n', ctypes.c_long(0)],
    [b'%.6D\n', ctypes.c_long(0)],
    [b'%hhD\n', ctypes.c_long(0)],
    [b'%llD\n', ctypes.c_long(0)],
    [b'%hD\n', ctypes.c_long(0)],
    [b'%lD\n', ctypes.c_long(0)],
    [b'%jD\n', ctypes.c_long(0)],
    [b'%zD\n', ctypes.c_long(0)],
]


mixed_cases = [
    [b'% 0+-#10.5llD', ctypes.c_long(42)],
]

test_sets = [
    {
        'name': 'D tests - basics.',
        'cases': basic_cases
    },
    {
        'name': 'D tests - basics.',
        'cases': mixed_cases
    }
]

cases_generator = generator_factory(test_sets)
