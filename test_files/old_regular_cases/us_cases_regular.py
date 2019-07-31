# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    [b'%S\n', None],
    [b'% S\n', None],
    [b'%0S\n', None],
    [b'%+S\n', None],
    [b'%-S\n', None],
    [b'%#S\n', None],
    [b'%10S\n', None],
    [b'%.5S\n', None],
    [b'%hhS\n', None],
    [b'%llS\n', None],
    [b'%jS\n', None],
    [b'%zS\n', None],
    [b'%hS\n', None],
    [b'%lS\n', None],
    [b'%S\n', ctypes.c_wchar_p('foo')],
    [b'% S\n', ctypes.c_wchar_p('foo')],
    [b'%0S\n', ctypes.c_wchar_p('foo')],
    [b'%+S\n', ctypes.c_wchar_p('foo')],
    [b'%-S\n', ctypes.c_wchar_p('foo')],
    [b'%#S\n', ctypes.c_wchar_p('foo')],
    [b'%10S\n', ctypes.c_wchar_p('foo')],
    [b'%.5S\n', ctypes.c_wchar_p('foo')],
    [b'%hhS\n', ctypes.c_wchar_p('foo')],
    [b'%llS\n', ctypes.c_wchar_p('foo')],
    [b'%jS\n', ctypes.c_wchar_p('foo')],
    [b'%zS\n', ctypes.c_wchar_p('foo')],
    [b'%hS\n', ctypes.c_wchar_p('foo')],
    [b'%lS\n', ctypes.c_wchar_p('foo')],
    [b'%S\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'% S\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%0S\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%+S\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%-S\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%#S\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%10S\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%.5S\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%hhS\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%llS\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%jS\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%zS\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%hS\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    [b'%lS\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
]

mixed_cases = [
    [b'% +0#-4.5hhS', ctypes.c_wchar_p(u'foo')],
]

test_sets = [
    {
        'name': 'S tests - basics.',
        'cases': basic_cases
    },
    {
        'name': 'S tests - mixed.',
        'cases': mixed_cases
    }
]

cases_generator = generator_factory(test_sets)
