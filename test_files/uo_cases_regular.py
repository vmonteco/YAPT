# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    [b'%O\n', ctypes.c_long(0)],
    [b'% O\n', ctypes.c_long(0)],
    [b'%+O\n', ctypes.c_long(0)],
    [b'%-O\n', ctypes.c_long(0)],
    [b'%0O\n', ctypes.c_long(0)],
    [b'%#O\n', ctypes.c_long(0)],
    [b'%10O\n', ctypes.c_long(0)],
    [b'%.6O\n', ctypes.c_long(0)],
    [b'%hhO\n', ctypes.c_long(0)],
    [b'%llO\n', ctypes.c_long(0)],
    [b'%hO\n', ctypes.c_long(0)],
    [b'%lO\n', ctypes.c_long(0)],
    [b'%jO\n', ctypes.c_long(0)],
    [b'%zO\n', ctypes.c_long(0)],
]


mixed_cases = [
    [b'% 0+-#10.5llO\n', ctypes.c_long(42)],
]

test_sets = [
    {
        'name': 'O tests - basics.',
        'cases': basic_cases
    },
    {
        'name': 'O tests - basics.',
        'cases': mixed_cases
    }
]

cases_generator = generator_factory(test_sets)
