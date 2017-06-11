#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ctypes
import itertools

# **************************************************************************** #
#                              Tool functions                                  #
# **************************************************************************** #

def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(len(s)+1)
    )

# **************************************************************************** #
#                                Limit values                                  #
# **************************************************************************** #

SHRT_MIN = -ctypes.c_ushort(-1).value // 2
SHRT_MAX = ctypes.c_ushort(-1).value // 2
USHRT_MAX = ctypes.c_ushort(-1).value
CHAR_MIN = -ctypes.c_ubyte(-1).value // 2
CHAR_MAX = ctypes.c_ubyte(-1).value // 2
UCHAR_MAX = ctypes.c_ubyte(-1).value
INT_MIN = -ctypes.c_uint(-1).value // 2
INT_MAX = ctypes.c_uint(-1).value // 2
UINT_MAX = ctypes.c_uint(-1).value
LONG_MIN = -ctypes.c_ulong(-1).value // 2
LONG_MAX = ctypes.c_ulong(-1).value // 2
ULONG_MAX = ctypes.c_ulong(-1).value
LLONG_MIN = -ctypes.c_ulonglong(-1).value // 2
LLONG_MAX = ctypes.c_ulonglong(-1).value // 2
ULLONG_MAX = ctypes.c_ulonglong(-1).value


# **************************************************************************** #
#                            format string elements                            #
# **************************************************************************** #


options = [b''.join(list(i)) for i in powerset([b' ', b'+', b'-', b'0', b'#'])]
min_len = [b'', b'0', b'1', b'2',  b'10']
precision = [b'', b'.', b'.0', b'.1', b'.2', b'.10']
len_mod = [b'', b'j', b'hh', b'll', b'l', b'h', b'z']
#conv_spec = [''] + [i for i in "cCsSpdDioOxXuU%a"]


# **************************************************************************** #
#                                   val sets                                   #
# **************************************************************************** #


pos_num_vals = [
    ctypes.c_short(0),
    ctypes.c_short(1),
    ctypes.c_short(SHRT_MAX),
    ctypes.c_ushort(USHRT_MAX),
    ctypes.c_byte(CHAR_MAX),
    ctypes.c_char(UCHAR_MAX),
    ctypes.c_int(INT_MAX),
    ctypes.c_uint(UINT_MAX),
    ctypes.c_long(LONG_MAX),
    ctypes.c_ulong(ULONG_MAX),
    ctypes.c_longlong(LLONG_MAX),
    ctypes.c_ulonglong(ULLONG_MAX),
]
neg_num_vals = [
    ctypes.c_short(-1),
    ctypes.c_short(SHRT_MIN),
    ctypes.c_byte(CHAR_MIN),
    ctypes.c_int(INT_MIN),
    ctypes.c_long(LONG_MIN),
    ctypes.c_longlong(LLONG_MIN),
]
char_vals = [
    ctypes.c_byte(0),
    ctypes.c_byte(-1),
    ctypes.c_byte(1),
    ctypes.c_byte(CHAR_MIN),
    ctypes.c_byte(CHAR_MAX),
    ctypes.c_char(0),
    ctypes.c_char(1),
    ctypes.c_char(UCHAR_MAX),
]
wchar_vals = [
    None,
    ctypes.c_wchar('a'),
    ctypes.c_wchar('\u262D'),
]
pointer_vals = [
    None,
    0,
    ctypes.c_uint(UINT_MAX),
    ctypes.c_ulonglong(ULLONG_MAX),
]
str_vals = [
    None,
    b'',
    b'c',
    b'foo',
]
wstr_vals = [
    None,
    ctypes.c_wchar_p(u''),
    ctypes.c_wchar_p(u'a'),
    ctypes.c_wchar_p(u'aaa'),
    ctypes.c_wchar_p(u'\u262D'),
    ctypes.c_wchar_p(u'\u262D\u262D\u262D'),
]


sets_set = [
    # (<name>, <conv_spec>, [<val_set keys>, ...]),
    ('percent tests', b'%', [None]),
    ('char tests', b'c', char_vals),
    ('wide char tests', b'C', wchar_vals),
    ('string tests', b's', str_vals),
    ('wide char string tests', b'S', wstr_vals),
    ('pointer tests', b'p', pointer_vals),
    ('d tests', b'd', pos_num_vals + neg_num_vals),
    ('D tests', b'D', pos_num_vals + neg_num_vals),
    ('i tests', b'i', pos_num_vals + neg_num_vals),
    ('o tests', b'o', pos_num_vals),
    ('O tests', b'O', pos_num_vals),
    ('x tests', b'x', pos_num_vals),
    ('X tests', b'X', pos_num_vals),
    ('u tests', b'u', pos_num_vals),
    ('U tests', b'U', pos_num_vals),
]

def all_cases():

    for s in sets_set:

        def f():
            for ml in min_len:
                for p in precision:
                    for lm in len_mod:
                        for v in s[2]:
                            for opt in options:
                                yield([b''.join([b'%', opt, ml, p, lm, s[1], b'\n']), v])

        yield({
            'name' : s[0],
            'cases' : f(),
        })

cmp_sets = all_cases()

segv_cases = [
]

segv_set = []

lks_set = []
