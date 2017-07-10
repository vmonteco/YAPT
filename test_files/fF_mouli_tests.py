# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

mouli_fuf_cases = [
    [b'{%f}{%F}', ctypes.c_float(1.42), ctypes.c_float(1.42)],
    [b'{%f}{%F}', ctypes.c_float(-1.42), ctypes.c_float(-1.42)],
    [b'{%f}{%F}', ctypes.c_float(1444565444646.6465424242242), ctypes.c_float(1444565444646.6465424242242)],
    [b'{%f}{%F}', ctypes.c_float(-1444565444646.6465424242242), ctypes.c_float(-1444565444646.6465424242242)],
]

test_sets = [
    {
        'name': 'moulitest\'s fF cases : bonus',
        'cases': mouli_fuf_cases,
    },
]

cases_generator = generator_factory(test_sets)
