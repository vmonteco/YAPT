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
    [b'%x\n', ctypes.c_int(1)],
    [b'% x\n', ctypes.c_int(1)],
    [b'%+x\n', ctypes.c_int(1)],
    [b'%-x\n', ctypes.c_int(1)],
    [b'%0x\n', ctypes.c_int(1)],
    [b'%#x\n', ctypes.c_int(1)],
    [b'%10x\n', ctypes.c_int(1)],
    [b'%.6x\n', ctypes.c_int(1)],
    [b'%hhx\n', ctypes.c_int(1)],
    [b'%llx\n', ctypes.c_int(1)],
    [b'%hx\n', ctypes.c_int(1)],
    [b'%lx\n', ctypes.c_int(1)],
    [b'%jx\n', ctypes.c_int(1)],
    [b'%zx\n', ctypes.c_int(1)],
    [b'%x\n', ctypes.c_int(123)],
    [b'% x\n', ctypes.c_int(123)],
    [b'%+x\n', ctypes.c_int(123)],
    [b'%-x\n', ctypes.c_int(123)],
    [b'%0x\n', ctypes.c_int(123)],
    [b'%#x\n', ctypes.c_int(123)],
    [b'%10x\n', ctypes.c_int(123)],
    [b'%.6x\n', ctypes.c_int(123)],
    [b'%hhx\n', ctypes.c_int(123)],
    [b'%llx\n', ctypes.c_int(123)],
    [b'%hx\n', ctypes.c_int(123)],
    [b'%lx\n', ctypes.c_int(123)],
    [b'%jx\n', ctypes.c_int(123)],
    [b'%zx\n', ctypes.c_int(123)],
]


mixed_cases = [
    [b'% 0+-#10.5llx\n', ctypes.c_int(42)],
    [b'%+-0#2x\\n', ctypes.c_short(0)],
    [b'%+-0#1x\\n', ctypes.c_short(1)],
    [b'%0#x\\n', ctypes.c_short(1)],
    [b'%01x\\n', ctypes.c_short(1)],
    [b'%#1x\\n', ctypes.c_short(1)],
    [b'%05x\\n', ctypes.c_short(1)],
    [b'%#5x\\n', ctypes.c_short(1)],
    [b'%#05x\\n', ctypes.c_short(1)],
    [b'%#04x\\n', ctypes.c_int(0xfffff)],
    [b'%#06x\\n', ctypes.c_int(0xfffff)],
    [b'%#01x\\n', ctypes.c_int(0xfffff)],
    [b'%#02x\\n', ctypes.c_int(0xfffff)],
    [b'%0#1x\\n', ctypes.c_short(0)],
    [b'%0#1x\\n', ctypes.c_short(1)],
    [b'%0#1x\\n', ctypes.c_short(10)],
    [b'%0#1x\\n', ctypes.c_short(133)],
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
