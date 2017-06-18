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
    [b'%c\n', ctypes.c_byte(-1)],
    [b'% c\n', ctypes.c_byte(-1)],
    [b'%+c\n', ctypes.c_byte(-1)],
    [b'%-c\n', ctypes.c_byte(-1)],
    [b'%#c\n', ctypes.c_byte(-1)],
    [b'%0c\n', ctypes.c_byte(-1)],
    [b'%10c\n', ctypes.c_byte(-1)],
    [b'%.5c\n', ctypes.c_byte(-1)],
    [b'%hhc\n', ctypes.c_byte(-1)],
    [b'%llc\n', ctypes.c_byte(-1)],
    [b'%hc\n', ctypes.c_byte(-1)],
    [b'%lc\n', ctypes.c_byte(-1)],
    [b'%zc\n', ctypes.c_byte(-1)],
    [b'%jc\n', ctypes.c_byte(-1)],
    [b'%c\n', ctypes.c_wchar(u'f')],
    [b'% c\n', ctypes.c_wchar(u'f')],
    [b'%+c\n', ctypes.c_wchar(u'f')],
    [b'%-c\n', ctypes.c_wchar(u'f')],
    [b'%#c\n', ctypes.c_wchar(u'f')],
    [b'%0c\n', ctypes.c_wchar(u'f')],
    [b'%10c\n', ctypes.c_wchar(u'f')],
    [b'%.5c\n', ctypes.c_wchar(u'f')],
    [b'%hhc\n', ctypes.c_wchar(u'f')],
    [b'%llc\n', ctypes.c_wchar(u'f')],
    [b'%hc\n', ctypes.c_wchar(u'f')],
    [b'%lc\n', ctypes.c_wchar(u'f')],
    [b'%zc\n', ctypes.c_wchar(u'f')],
    [b'%jc\n', ctypes.c_wchar(u'f')],
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
    [b'%c\n', ctypes.c_wchar(u'\0')],
    [b'% c\n', ctypes.c_wchar(u'\0')],
    [b'%+c\n', ctypes.c_wchar(u'\0')],
    [b'%-c\n', ctypes.c_wchar(u'\0')],
    [b'%#c\n', ctypes.c_wchar(u'\0')],
    [b'%0c\n', ctypes.c_wchar(u'\0')],
    [b'%10c\n', ctypes.c_wchar(u'\0')],
    [b'%.5c\n', ctypes.c_wchar(u'\0')],
    [b'%hhc\n', ctypes.c_wchar(u'\0')],
    [b'%llc\n', ctypes.c_wchar(u'\0')],
    [b'%hc\n', ctypes.c_wchar(u'\0')],
    [b'%lc\n', ctypes.c_wchar(u'\0')],
    [b'%zc\n', ctypes.c_wchar(u'\0')],
    [b'%jc\n', ctypes.c_wchar(u'\0')],
    
    [b'%c\n', ctypes.c_wchar(u'\u262D')],
    [b'% c\n', ctypes.c_wchar(u'\u262D')],
    [b'%+c\n', ctypes.c_wchar(u'\u262D')],
    [b'%-c\n', ctypes.c_wchar(u'\u262D')],
    [b'%#c\n', ctypes.c_wchar(u'\u262D')],
    [b'%0c\n', ctypes.c_wchar(u'\u262D')],
    [b'%10c\n', ctypes.c_wchar(u'\u262D')],
    [b'%.5c\n', ctypes.c_wchar(u'\u262D')],
    [b'%hhc\n', ctypes.c_wchar(u'\u262D')],
    [b'%llc\n', ctypes.c_wchar(u'\u262D')],
    [b'%hc\n', ctypes.c_wchar(u'\u262D')],
    [b'%lc\n', ctypes.c_wchar(u'\u262D')],
    [b'%zc\n', ctypes.c_wchar(u'\u262D')],
    [b'%jc\n', ctypes.c_wchar(u'\u262D')],
]

mixed_cases = [
    [b'%2lc\n', ctypes.c_wchar(u'\u262D')],
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
