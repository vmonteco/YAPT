# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    [b'%x\n', ctypes.c_int(0)],
    [b'% x\n', ctypes.c_int(0)],
    [b'%+x\n', ctypes.c_int(0)],
    [b'%-x\n', ctypes.c_int(0)],
    [b'%0x\n', ctypes.c_int(0)],
    [b'%#x\n', ctypes.c_int(0)],
    [b'%10x\n', ctypes.c_int(0)],
    [b'%.6x\n', ctypes.c_int(0)],
    [b'%hhx\n', ctypes.c_int(0)],
    [b'%llx\n', ctypes.c_int(0)],
    [b'%hx\n', ctypes.c_int(0)],
    [b'%lx\n', ctypes.c_int(0)],
    [b'%jx\n', ctypes.c_int(0)],
    [b'%zx\n', ctypes.c_int(0)],
]


mixed_cases = [
    [b'% 0+-#10.5llx\n', ctypes.c_int(42)],
]

test_sets = [
    {
        'name': 'x tests - basics.',
        'cases': basic_cases
    },
    {
        'name': 'x tests - basics.',
        'cases': mixed_cases
    }
]

cases_generator = generator_factory(test_sets)
