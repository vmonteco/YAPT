# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import ctypes

basic_cases = [
    [b'%c\n', ctypes.c_char(b'f')],
    [b'% c\n', ctypes.c_char(b'f')],
    [b'%+c\n', ctypes.c_char(b'f')],
    [b'%-c\n', ctypes.c_char(b'f')],
    [b'%#c\n', ctypes.c_char(b'f')],
    [b'%0c\n', ctypes.c_char(b'f')],
    [b'%10c\n', ctypes.c_char(b'f')],
    [b'%.5c\n', ctypes.c_char(b'f')],
    [b'%hhc\n', ctypes.c_char(b'f')],
    [b'%llc\n', ctypes.c_char(b'f')],
    [b'%hc\n', ctypes.c_char(b'f')],
    [b'%lc\n', ctypes.c_char(b'f')],
    [b'%zc\n', ctypes.c_char(b'f')],
    [b'%jc\n', ctypes.c_char(b'f')],
    [u'%c\n', ctypes.c_wchar(u'f')],
    [u'% c\n', ctypes.c_wchar(u'f')],
    [u'%+c\n', ctypes.c_wchar(u'f')],
    [u'%-c\n', ctypes.c_wchar(u'f')],
    [u'%#c\n', ctypes.c_wchar(u'f')],
    [u'%0c\n', ctypes.c_wchar(u'f')],
    [u'%10c\n', ctypes.c_wchar(u'f')],
    [u'%.5c\n', ctypes.c_wchar(u'f')],
    [u'%hhc\n', ctypes.c_wchar(u'f')],
    [u'%llc\n', ctypes.c_wchar(u'f')],
    [u'%hc\n', ctypes.c_wchar(u'f')],
    [u'%lc\n', ctypes.c_wchar(u'f')],
    [u'%zc\n', ctypes.c_wchar(u'f')],
    [u'%jc\n', ctypes.c_wchar(u'f')],
    [b'%c\n', ctypes.c_char(b'\0')],
    [b'% c\n', ctypes.c_char(b'\0')],
    [b'%+c\n', ctypes.c_char(b'\0')],
    [b'%-c\n', ctypes.c_char(b'\0')],
    [b'%#c\n', ctypes.c_char(b'\0')],
    [b'%0c\n', ctypes.c_char(b'\0')],
    [b'%10c\n', ctypes.c_char(b'\0')],
    [b'%.5c\n', ctypes.c_char(b'\0')],
    [b'%hhc\n', ctypes.c_char(b'\0')],
    [b'%llc\n', ctypes.c_char(b'\0')],
    [b'%hc\n', ctypes.c_char(b'\0')],
    [b'%lc\n', ctypes.c_char(b'\0')],
    [b'%zc\n', ctypes.c_char(b'\0')],
    [b'%jc\n', ctypes.c_char(b'\0')],
    [u'%c\n', ctypes.c_wchar(u'\0')],
    [u'% c\n', ctypes.c_wchar(u'\0')],
    [u'%+c\n', ctypes.c_wchar(u'\0')],
    [u'%-c\n', ctypes.c_wchar(u'\0')],
    [u'%#c\n', ctypes.c_wchar(u'\0')],
    [u'%0c\n', ctypes.c_wchar(u'\0')],
    [u'%10c\n', ctypes.c_wchar(u'\0')],
    [u'%.5c\n', ctypes.c_wchar(u'\0')],
    [u'%hhc\n', ctypes.c_wchar(u'\0')],
    [u'%llc\n', ctypes.c_wchar(u'\0')],
    [u'%hc\n', ctypes.c_wchar(u'\0')],
    [u'%lc\n', ctypes.c_wchar(u'\0')],
    [u'%zc\n', ctypes.c_wchar(u'\0')],
    [u'%jc\n', ctypes.c_wchar(u'\0')],
    [u'%c\n', ctypes.c_wchar(u'\u262D')],
    [u'% c\n', ctypes.c_wchar(u'\u262D')],
    [u'%+c\n', ctypes.c_wchar(u'\u262D')],
    [u'%-c\n', ctypes.c_wchar(u'\u262D')],
    [u'%#c\n', ctypes.c_wchar(u'\u262D')],
    [u'%0c\n', ctypes.c_wchar(u'\u262D')],
    [u'%10c\n', ctypes.c_wchar(u'\u262D')],
    [u'%.5c\n', ctypes.c_wchar(u'\u262D')],
    [u'%hhc\n', ctypes.c_wchar(u'\u262D')],
    [u'%llc\n', ctypes.c_wchar(u'\u262D')],
    [u'%hc\n', ctypes.c_wchar(u'\u262D')],
    [u'%lc\n', ctypes.c_wchar(u'\u262D')],
    [u'%zc\n', ctypes.c_wchar(u'\u262D')],
    [u'%jc\n', ctypes.c_wchar(u'\u262D')],
]

mixed_cases = [
    ['% +0#-4.5hhc\n', ctypes.c_char(b'f')],
]

test_sets = [
    {
        'name': 'c tests - basics.',
        'cases': basic_cases
    },
    {
        'name': 'c tests - mixed.',
        'cases': mixed_cases
    }
]

cases_generator = generator_factory(test_sets)
