# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    [b'%s\n', None],
    [b'% s\n', None],
    [b'%0s\n', None],
    [b'%+s\n', None],
    [b'%-s\n', None],
    [b'%#s\n', None],
    [b'%10s\n', None],
    [b'%.5s\n', None],
    [b'%hhs\n', None],
    [b'%lls\n', None],
    [b'%js\n', None],
    [b'%zs\n', None],
    [b'%hs\n', None],
    [b'%ls\n', None],
    [b'%s\n', b'foo'],
    [b'% s\n', b'foo'],
    [b'%0s\n', b'foo'],
    [b'%+s\n', b'foo'],
    [b'%-s\n', b'foo'],
    [b'%#s\n', b'foo'],
    [b'%10s\n', b'foo'],
    [b'%.5s\n', b'foo'],
    [b'%hhs\n', b'foo'],
    [b'%lls\n', b'foo'],
    [b'%js\n', b'foo'],
    [b'%zs\n', b'foo'],
    [b'%hs\n', b'foo'],
    [b'%ls\n', ctypes.c_wchar_p(u'foo')],
    [b'%s\n', ctypes.c_wchar_p(u'\u262Dbar\u262D')],
    [b'% s\n', ctypes.c_wchar_p(u'\u262Dbar\u262D')],
    [b'%0s\n', ctypes.c_wchar_p(u'\u262Dbar\u262D')],
    [b'%+s\n', ctypes.c_wchar_p(u'\u262Dbar\u262D')],
    [b'%-s\n', ctypes.c_wchar_p(u'\u262Dbar\u262D')],
    [b'%#s\n', ctypes.c_wchar_p(u'\u262Dbar\u262D')],
    [b'%10s\n', ctypes.c_wchar_p(u'\u262Dbar\u262D')],
    [b'%.5s\n', ctypes.c_wchar_p(u'\u262Dbar\u262D')],
    [b'%hhs\n', ctypes.c_wchar_p(u'\u262Dbar\u262D')],
    [b'%lls\n', ctypes.c_wchar_p(u'\u262Dbar\u262D')],
    [b'%js\n', ctypes.c_wchar_p(u'\u262Dbar\u262D')],
    [b'%zs\n', ctypes.c_wchar_p(u'\u262Dbar\u262D')],
    [b'%hs\n', ctypes.c_wchar_p(u'\u262Dbar\u262D')],
    [b'%ls\n', ctypes.c_wchar_p(u'\u262Dbar\u262D')],
]

mixed_cases = [
    [b'% +0#-4.5hhs', b'foo'],
    [b'%.4s\n', b'foo'],
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
