# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

mouli_1_cases = [
    [b'%*d', ctypes.c_int(5), ctypes.c_int(42)],
    [b'{%*d}', ctypes.c_int(-5), ctypes.c_int(42)],
    [b'{%*d}', ctypes.c_int(0), ctypes.c_int(42)],
    [b'{%*c}', ctypes.c_int(0), ctypes.c_int(0)],
    [b'{%*c}', ctypes.c_int(-15), ctypes.c_int(0)],
    [b'{%*d}', ctypes.c_int(5), ctypes.c_int(42)],
    [b'{%*d}', ctypes.c_int(-5), ctypes.c_int(42)],
    [b'{%*d}', ctypes.c_int(0), ctypes.c_int(42)],
    [b'{%*s}', ctypes.c_int(5), b'42'],
    [b'{%*s}', ctypes.c_int(-5), b'42'],
    [b'{%*s}', ctypes.c_int(0), b'42'],
    [b'{%*s}', ctypes.c_int(5), ctypes.c_int(0)],
    [b'{%3*p}', ctypes.c_int(10), ctypes.c_int(0)],
]

mouli_2_cases = [
    [b'%*.*d', ctypes.c_int(0), ctypes.c_int(3), ctypes.c_int(0)],
]

mouli_3_cases = [
    [b'{%3*d}', ctypes.c_int(0), ctypes.c_int(0)],
    [b'{%*3d}', ctypes.c_int(0), ctypes.c_int(0)],
    [b'{%*3d}', ctypes.c_int(5), ctypes.c_int(0)],
    [b'{%05.*d}', ctypes.c_int(-15), ctypes.c_int(42)],
]

test_sets = [
    {
        'name': 'moulitest\'s wildcard cases : bonus 1',
        'cases': mouli_1_cases,
    },
    {
        'name': 'moulitest\'s wildcard cases : bonus 2',
        'cases': mouli_2_cases,
    }
]

cases_generator = generator_factory(test_sets)
