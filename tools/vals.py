# -*- coding: utf-8 -*-

import ctypes
from tools.limits import *

pos_num_vals = [
    [ctypes.c_short(0)],
    [ctypes.c_short(1)],
    [ctypes.c_short(SHRT_MAX)],
    [ctypes.c_ushort(USHRT_MAX)],
    [ctypes.c_byte(CHAR_MAX)],
    [ctypes.c_char(UCHAR_MAX)],
    [ctypes.c_int(INT_MAX)],
    [ctypes.c_uint(UINT_MAX)],
    [ctypes.c_long(LONG_MAX)],
    [ctypes.c_ulong(ULONG_MAX)],
    [ctypes.c_longlong(LLONG_MAX)],
    [ctypes.c_ulonglong(ULLONG_MAX)],
]
neg_num_vals = [
    [ctypes.c_short(-1)],
    [ctypes.c_short(SHRT_MIN)],
    [ctypes.c_byte(CHAR_MIN)],
    [ctypes.c_int(INT_MIN)],
    [ctypes.c_long(LONG_MIN)],
    [ctypes.c_longlong(LLONG_MIN)],
]
char_vals = [
    [ctypes.c_byte(0)],
    [ctypes.c_byte(-1)],
    [ctypes.c_byte(1)],
    [ctypes.c_byte(CHAR_MIN)],
    [ctypes.c_byte(CHAR_MAX)],
    [ctypes.c_char(0)],
    [ctypes.c_char(1)],
    [ctypes.c_char(UCHAR_MAX)],
]
wchar_vals = [
    [None],
    [ctypes.c_wchar('a')],
    [ctypes.c_wchar('\u262D')],
]
pointer_vals = [
    [None],
    [0],
    [ctypes.c_uint(UINT_MAX)],
    [ctypes.c_ulonglong(ULLONG_MAX)],
]
str_vals = [
    [None],
    [b''],
    [b'c'],
    [b'foo'],
]
wstr_vals = [
    [None],
    [ctypes.c_wchar_p(u'')],
    [ctypes.c_wchar_p(u'a')],
    [ctypes.c_wchar_p(u'aaa')],
    [ctypes.c_wchar_p(u'\u262D')],
    [ctypes.c_wchar_p(u'\u262D\u262D\u262D')],
]

