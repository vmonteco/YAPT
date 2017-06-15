# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    ['%S\n', None],
    ['% S\n', None],
    ['%0S\n', None],
    ['%+S\n', None],
    ['%-S\n', None],
    ['%#S\n', None],
    ['%10S\n', None],
    ['%.5S\n', None],
    ['%hhS\n', None],
    ['%llS\n', None],
    ['%jS\n', None],
    ['%zS\n', None],
    ['%hS\n', None],
    ['%lS\n', None],
    ['%S\n', ctypes.c_wchar_p('foo')],
    ['% S\n', ctypes.c_wchar_p('foo')],
    ['%0S\n', ctypes.c_wchar_p('foo')],
    ['%+S\n', ctypes.c_wchar_p('foo')],
    ['%-S\n', ctypes.c_wchar_p('foo')],
    ['%#S\n', ctypes.c_wchar_p('foo')],
    ['%10S\n', ctypes.c_wchar_p('foo')],
    ['%.5S\n', ctypes.c_wchar_p('foo')],
    ['%hhS\n', ctypes.c_wchar_p('foo')],
    ['%llS\n', ctypes.c_wchar_p('foo')],
    ['%jS\n', ctypes.c_wchar_p('foo')],
    ['%zS\n', ctypes.c_wchar_p('foo')],
    ['%hS\n', ctypes.c_wchar_p('foo')],
    ['%lS\n', ctypes.c_wchar_p('foo')],
    ['%S\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['% S\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%0S\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%+S\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%-S\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%#S\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%10S\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%.5S\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%hhS\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%llS\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%jS\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%zS\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%hS\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
    ['%lS\n', ctypes.c_wchar_p('\u262Dbar\u262D')],
]

mixed_cases = [
    ['% +0#-4.5hhS', ctypes.c_wchar_p(u'foo')],
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
