# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    [b'%p\n', None],
    [b'% p\n', None],
    [b'%0p\n', None],
    [b'%+p\n', None],
    [b'%-p\n', None],
    [b'%#p\n', None],
    [b'%10p\n', None],
    [b'%.5p\n', None],
    [b'%hhp\n', None],
    [b'%llp\n', None],
    [b'%jp\n', None],
    [b'%zp\n', None],
    [b'%hp\n', None],
    [b'%lp\n', None],
    [b'%p\n', b'foo'],
    [b'% p\n', b'foo'],
    [b'%0p\n', b'foo'],
    [b'%+p\n', b'foo'],
    [b'%-p\n', b'foo'],
    [b'%#p\n', b'foo'],
    [b'%10p\n', b'foo'],
    [b'%.5p\n', b'foo'],
    [b'%hhp\n', b'foo'],
    [b'%llp\n', b'foo'],
    [b'%jp\n', b'foo'],
    [b'%zp\n', b'foo'],
    [b'%hp\n', b'foo'],
    [b'%lp\n', b'foo'],
    [b'%p\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'% p\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%0p\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%+p\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%-p\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%#p\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%10p\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%.5p\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%hhp\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%llp\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%jp\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%zp\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%hp\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%lp\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
]

mixed_cases = [
    [b'% +0#-4.5hhp', b'foo'],
]

test_sets = [
    {
        'name': 'p tests - basics.',
        'cases': basic_cases
    },
    {
        'name': 'p tests - mixed.',
        'cases': mixed_cases
    }
]

cases_generator = generator_factory(test_sets)
