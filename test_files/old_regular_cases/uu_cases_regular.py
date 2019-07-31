# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    [b'%U\n', ctypes.c_long(0)],
    [b'% U\n', ctypes.c_long(0)],
    [b'%+U\n', ctypes.c_long(0)],
    [b'%-U\n', ctypes.c_long(0)],
    [b'%0U\n', ctypes.c_long(0)],
    [b'%#U\n', ctypes.c_long(0)],
    [b'%10U\n', ctypes.c_long(0)],
    [b'%.6U\n', ctypes.c_long(0)],
    [b'%hhU\n', ctypes.c_long(0)],
    [b'%llU\n', ctypes.c_long(0)],
    [b'%hU\n', ctypes.c_long(0)],
    [b'%lU\n', ctypes.c_long(0)],
    [b'%jU\n', ctypes.c_long(0)],
    [b'%zU\n', ctypes.c_long(0)],
]


mixed_cases = [
    [b'%-02U\n', ctypes.c_short(0)],
    [b'% 0+-#10.5llU\n', ctypes.c_long(42)],
]

test_sets = [
    {
        'name': 'U tests - basics.',
        'cases': basic_cases
    },
    {
        'name': 'U tests - basics.',
        'cases': mixed_cases
    }
]

cases_generator = generator_factory(test_sets)
