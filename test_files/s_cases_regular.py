# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    ['%s\n', None],
    ['% s\n', None],
    ['%0s\n', None],
    ['%+s\n', None],
    ['%-s\n', None],
    ['%#s\n', None],
    ['%10s\n', None],
    ['%.5s\n', None],
    ['%hhs\n', None],
    ['%lls\n', None],
    ['%js\n', None],
    ['%zs\n', None],
    ['%hs\n', None],
    ['%ls\n', None],
    ['%s\n', b'foo'],
    ['% s\n', b'foo'],
    ['%0s\n', b'foo'],
    ['%+s\n', b'foo'],
    ['%-s\n', b'foo'],
    ['%#s\n', b'foo'],
    ['%10s\n', b'foo'],
    ['%.5s\n', b'foo'],
    ['%hhs\n', b'foo'],
    ['%lls\n', b'foo'],
    ['%js\n', b'foo'],
    ['%zs\n', b'foo'],
    ['%hs\n', b'foo'],
    ['%ls\n', b'foo'],
    ['%s\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['% s\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%0s\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%+s\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%-s\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%#s\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%10s\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%.5s\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%hhs\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%lls\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%js\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%zs\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%hs\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%ls\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
]

mixed_cases = [
    ['% +0#-4.5hhs', b'foo'],
]

test_sets = [
    {
        'name': 's tests - basics.',
        'cases': basic_cases
    },
    {
        'name': 's tests - mixed.',
        'cases': mixed_cases
    }
]

cases_generator = generator_factory(test_sets)
