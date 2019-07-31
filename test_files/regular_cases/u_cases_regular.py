# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    [b'%u\n', ctypes.c_int(0)],
    [b'% u\n', ctypes.c_int(0)],
    [b'%+u\n', ctypes.c_int(0)],
    [b'%-u\n', ctypes.c_int(0)],
    [b'%0u\n', ctypes.c_int(0)],
    [b'%#u\n', ctypes.c_int(0)],
    [b'%10u\n', ctypes.c_int(0)],
    [b'%.6u\n', ctypes.c_int(0)],
    [b'%hhu\n', ctypes.c_int(0)],
    [b'%llu\n', ctypes.c_int(0)],
    [b'%hu\n', ctypes.c_int(0)],
    [b'%lu\n', ctypes.c_int(0)],
    [b'%ju\n', ctypes.c_int(0)],
    [b'%zu\n', ctypes.c_int(0)],
]


mixed_cases = [
    [b'% 010u\n', ctypes.c_short(0)],
    [b'% 02u\n', ctypes.c_short(0)],
    [b'%01.u\n', ctypes.c_short(0)],
    [b'%02u\n', ctypes.c_short(0)],
    [b'%+-0#2u\n', ctypes.c_short(0)],
    [b'% 0+-#10.5llu\n', ctypes.c_int(42)],
]

test_sets = [
    {
        'name': 'u tests - basics.',
        'cases': basic_cases
    },
    {
        'name': 'u tests - basics.',
        'cases': mixed_cases
    }
]

cases_generator = generator_factory(test_sets)
