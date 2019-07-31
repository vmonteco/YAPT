# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    [b'%d\n', ctypes.c_int(0)],
    [b'% d\n', ctypes.c_int(0)],
    [b'%+d\n', ctypes.c_int(0)],
    [b'%-d\n', ctypes.c_int(0)],
    [b'%0d\n', ctypes.c_int(0)],
    [b'%#d\n', ctypes.c_int(0)],
    [b'%10d\n', ctypes.c_int(0)],
    [b'%.6d\n', ctypes.c_int(0)],
    [b'%hhd\n', ctypes.c_int(0)],
    [b'%lld\n', ctypes.c_int(0)],
    [b'%hd\n', ctypes.c_int(0)],
    [b'%ld\n', ctypes.c_int(0)],
    [b'%jd\n', ctypes.c_int(0)],
    [b'%zd\n', ctypes.c_int(0)],
]


mixed_cases = [
    [b'% 0+-#10.5lld', ctypes.c_int(42)],
]

test_sets = [
    {
        'name': 'd tests - basics.',
        'cases': basic_cases
    },
    {
        'name': 'd tests - basics.',
        'cases': mixed_cases
    }
]

cases_generator = generator_factory(test_sets)
