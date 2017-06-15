# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    [b'%X\n', ctypes.c_long(0)],
    [b'% X\n', ctypes.c_long(0)],
    [b'%+X\n', ctypes.c_long(0)],
    [b'%-X\n', ctypes.c_long(0)],
    [b'%0X\n', ctypes.c_long(0)],
    [b'%#X\n', ctypes.c_long(0)],
    [b'%10X\n', ctypes.c_long(0)],
    [b'%.6X\n', ctypes.c_long(0)],
    [b'%hhX\n', ctypes.c_long(0)],
    [b'%llX\n', ctypes.c_long(0)],
    [b'%hX\n', ctypes.c_long(0)],
    [b'%lX\n', ctypes.c_long(0)],
    [b'%jX\n', ctypes.c_long(0)],
    [b'%zX\n', ctypes.c_long(0)],
]


mixed_cases = [
    [b'% 0+-#10.5llX\n', ctypes.c_long(42)],
]

test_sets = [
    {
        'name': 'X tests - basics.',
        'cases': basic_cases
    },
    {
        'name': 'X tests - basics.',
        'cases': mixed_cases
    }
]

cases_generator = generator_factory(test_sets)
