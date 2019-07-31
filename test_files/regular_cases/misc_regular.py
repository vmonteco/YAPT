# -*- coding:  utf-8 -*-

from tools.factories import generator_factory
import ctypes

length_cases = [
    [b''.join([b'a' for i in range(4095)])],
]

segv_cases = [
    [b'%',],
    [b'% Zoooo',],
    [b'{%}',],
    [b'{%10R}',],
    [b'{%03c}',],
    [b'{%-15Z}', ctypes.c_int(123)],
    [b'{%05.c}', ctypes.c_int(0)],
    [b'{%05.%}', ctypes.c_int(0)],
    [b'{%05.Z}', ctypes.c_int(0)],
    
]

test_sets = [
    {
        'name': 'lenght test',
        'cases': length_cases
    },
    {
        'name': 'segv tests',
        'cases': segv_cases
    },
]

cases_generator = generator_factory(test_sets)
