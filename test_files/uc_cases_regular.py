# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    [b'%C\n', ctypes.c_wchar(u'\u262D')],
    [b'% C\n', ctypes.c_wchar(u'\u262D')],
    [b'%+C\n', ctypes.c_wchar(u'\u262D')],
    [b'%#C\n', ctypes.c_wchar(u'\u262D')],
    [b'%0C\n', ctypes.c_wchar(u'\u262D')],
    [b'%-C\n', ctypes.c_wchar(u'\u262D')],
    [b'%10C\n', ctypes.c_wchar(u'\u262D')],
    [b'%.5C\n', ctypes.c_wchar(u'\u262D')],
    [b'%hhC\n', ctypes.c_wchar(u'\u262D')],
    [b'%llC\n', ctypes.c_wchar(u'\u262D')],
    [b'%hC\n', ctypes.c_wchar(u'\u262D')],
    [b'%lC\n', ctypes.c_wchar(u'\u262D')],
    [b'%jC\n', ctypes.c_wchar(u'\u262D')],
    [b'%zC\n', ctypes.c_wchar(u'\u262D')],
    [b'%C\n', ctypes.c_wchar('a')],
    [b'% C\n', ctypes.c_wchar('a')],
    [b'%+C\n', ctypes.c_wchar('a')],
    [b'%#C\n', ctypes.c_wchar('a')],
    [b'%0C\n', ctypes.c_wchar('a')],
    [b'%-C\n', ctypes.c_wchar('a')],
    [b'%10C\n', ctypes.c_wchar('a')],
    [b'%.5C\n', ctypes.c_wchar('a')],
    [b'%hhC\n', ctypes.c_wchar('a')],
    [b'%llC\n', ctypes.c_wchar('a')],
    [b'%hC\n', ctypes.c_wchar('a')],
    [b'%lC\n', ctypes.c_wchar('a')],
    [b'%jC\n', ctypes.c_wchar('a')],
    [b'%zC\n', ctypes.c_wchar('a')],
    [b'%C\n', ctypes.c_wchar('\0')],
    [b'% C\n', ctypes.c_wchar('\0')],
    [b'%+C\n', ctypes.c_wchar('\0')],
    [b'%#C\n', ctypes.c_wchar('\0')],
    [b'%0C\n', ctypes.c_wchar('\0')],
    [b'%-C\n', ctypes.c_wchar('\0')],
    [b'%10C\n', ctypes.c_wchar('\0')],
    [b'%.5C\n', ctypes.c_wchar('\0')],
    [b'%hhC\n', ctypes.c_wchar('\0')],
    [b'%llC\n', ctypes.c_wchar('\0')],
    [b'%hC\n', ctypes.c_wchar('\0')],
    [b'%lC\n', ctypes.c_wchar('\0')],
    [b'%jC\n', ctypes.c_wchar('\0')],
    [b'%zC\n', ctypes.c_wchar('\0')],
]

mixed_cases = [
    ['% +0#-4.5hhC\n', ctypes.c_wchar(u'f')],
    ['% +0#-4.5hhC\n', ctypes.c_wchar(u'\u262D')],
    ['% +0#-4.5hhC\n', ctypes.c_wchar(u'\0')],
]

test_sets = [
    {
        'name': 'C tests - basics.',
        'cases': basic_cases
    },
    {
        'name': 'C tests - mixed.',
        'cases': mixed_cases
    }
]

cases_generator = generator_factory(test_sets)
