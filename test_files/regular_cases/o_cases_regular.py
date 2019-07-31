# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    [b'%o\n', ctypes.c_int(0)],
    [b'% o\n', ctypes.c_int(0)],
    [b'%+o\n', ctypes.c_int(0)],
    [b'%-o\n', ctypes.c_int(0)],
    [b'%0o\n', ctypes.c_int(0)],
    [b'%#o\n', ctypes.c_int(0)],
    [b'%10o\n', ctypes.c_int(0)],
    [b'%.6o\n', ctypes.c_int(0)],
    [b'%hho\n', ctypes.c_int(0)],
    [b'%llo\n', ctypes.c_int(0)],
    [b'%ho\n', ctypes.c_int(0)],
    [b'%lo\n', ctypes.c_int(0)],
    [b'%jo\n', ctypes.c_int(0)],
    [b'%zo\n', ctypes.c_int(0)],
]


mixed_cases = [
    [b'%#10.10o\n', ctypes.c_short(0)],
    [b'%#1.o\n', ctypes.c_short(0)],
    [b'%#.o\n', ctypes.c_char(b'\xff')],
    [b'%#.0o\n', ctypes.c_char(b'\xff')],
    [b'%#.1o\n', ctypes.c_char(b'\xff')],
    [b'%#.1o\n', ctypes.c_short(0)],
    [b'%#.2o\n', ctypes.c_short(0)],
    [b'% 0+-#10.5llo\n', ctypes.c_int(42)],
]

test_sets = [
    {
        'name': 'o tests - basics.',
        'cases': basic_cases
    },
    {
        'name': 'o tests - basics.',
        'cases': mixed_cases
    }
]

cases_generator = generator_factory(test_sets)
