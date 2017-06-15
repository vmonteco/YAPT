# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    ['%p\n', None],
    ['% p\n', None],
    ['%0p\n', None],
    ['%+p\n', None],
    ['%-p\n', None],
    ['%#p\n', None],
    ['%10p\n', None],
    ['%.5p\n', None],
    ['%hhp\n', None],
    ['%llp\n', None],
    ['%jp\n', None],
    ['%zp\n', None],
    ['%hp\n', None],
    ['%lp\n', None],
    ['%p\n', b'foo'],
    ['% p\n', b'foo'],
    ['%0p\n', b'foo'],
    ['%+p\n', b'foo'],
    ['%-p\n', b'foo'],
    ['%#p\n', b'foo'],
    ['%10p\n', b'foo'],
    ['%.5p\n', b'foo'],
    ['%hhp\n', b'foo'],
    ['%llp\n', b'foo'],
    ['%jp\n', b'foo'],
    ['%zp\n', b'foo'],
    ['%hp\n', b'foo'],
    ['%lp\n', b'foo'],
    ['%p\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['% p\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%0p\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%+p\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%-p\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%#p\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%10p\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%.5p\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%hhp\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%llp\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%jp\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%zp\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%hp\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%lp\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
]

mixed_cases = [
    ['% +0#-4.5hhp', b'foo'],
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
