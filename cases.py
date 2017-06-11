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
#                               Basics elements                                #
# **************************************************************************** #

options = " +#0-"
min_len = ['0', '1', '-1', '100', '-100', 'bar']
precision = ['0', '1', '-1', '100', '-100', 'bar']
len_mod = ['', 'j', 'hh', 'll', 'l', 'h', 'z', 'bar']
conv_spec = list("cCsSpdDioOxXuU%")
vals = [
    None,    
    b'foo',
    b'bar',
    b'',
    ctypes.c_wchar(u'\u262D'),
    ctypes.c_short(0),
    ctypes.c_short(-1),
    ctypes.c_short(1),
    ctypes.c_short(SHRT_MIN),
    ctypes.c_short(SHRT_MAX),
    ctypes.c_ushort(0),
    ctypes.c_ushort(1),
    ctypes.c_ushort(USHRT_MAX),
    ctypes.c_byte(0),
    ctypes.c_byte(-1),
    ctypes.c_byte(1),
    ctypes.c_byte(CHAR_MIN),
    ctypes.c_byte(CHAR_MAX),
    ctypes.c_char(0),
    ctypes.c_char(1),
    ctypes.c_char(UCHAR_MAX),
    ctypes.c_int(0),
    ctypes.c_int(-1),
    ctypes.c_int(1),
    ctypes.c_int(INT_MIN),
    ctypes.c_int(INT_MAX),
    ctypes.c_uint(0),
    ctypes.c_uint(1),
    ctypes.c_uint(UINT_MAX),
    ctypes.c_long(0),
    ctypes.c_long(-1),
    ctypes.c_long(1),
    ctypes.c_long(LONG_MIN),
    ctypes.c_long(LONG_MAX),
    ctypes.c_ulong(0),
    ctypes.c_ulong(1),
    ctypes.c_ulong(ULONG_MAX),
    ctypes.c_longlong(0),
    ctypes.c_longlong(-1),
    ctypes.c_longlong(1),
    ctypes.c_longlong(LLONG_MIN),
    ctypes.c_longlong(LLONG_MAX),
    ctypes.c_ulonglong(0),
    ctypes.c_ulonglong(1),
    ctypes.c_ulonglong(ULLONG_MAX),
]


# **************************************************************************** #
#                              comparison cases                                #
# **************************************************************************** #

cmp_raw_cases = [
    [None],
    [b''],
    [b'foo'],
]

cmp_percent_cases = [
    [b'%%'],
    [b'foo%%'],
    [b'%%bar'],
    [b'foo%%bar'],
    [b'fop%%bar%%foo'],
]

cmp_c_cases = [
    [b'%c', ctypes.c_char(b'a')],
    [b'%5c', ctypes.c_char(b'a')],
    [b'%-c', ctypes.c_char(b'a')],
    [b'%-5c', ctypes.c_char(b'a')],
    [b'%lc', ctypes.c_wchar('\u262D')],
    [b'%5lc', ctypes.c_wchar('\u262D')],
    [b'%-lc', ctypes.c_wchar('\u262D')],
    [b'%-5lc', ctypes.c_wchar('\u262D')],
]

cmp_uc_cases = [
    [b'%c', ctypes.c_wchar('a')],
    [b'%5c', ctypes.c_wchar('a')],
    [b'%-c', ctypes.c_wchar('a')],
    [b'%-5c', ctypes.c_wchar('a')],
    [b'%lc', ctypes.c_wchar('\u262D')],
    [b'%5lc', ctypes.c_wchar('\u262D')],
    [b'%-lc', ctypes.c_wchar('\u262D')],
    [b'%-5lc', ctypes.c_wchar('\u262D')],
]

#cmp_s_cases = []

def cmp_s_cases():
    s_vals = [
        None,
        b'',
        b'c',
        b'foo',
        b'foobar\n',
    ]
    us_vals = [
        None,
        u'',
        u'a',
        u'\u262D',
        u'foo\u262D\u262D',
    ]
    s_options = [b'', b'-']
    min_len = [b'', b'0', b'1', b'5', b'10']
    precision = [b'', b'.', b'.1', b'.4', b'.5', b'.6', b'.10']
    len_mod = [b'', b'hh', b'll', b'h', b'l', b'j', b'z']
    for opt in s_options:
        for ml in min_len:
            for p in precision:
                for lm in len_mod:
                    for v in s_vals:
                        res = [
                            b'%' + opt + ml + p +lm + b's',
                            v
                        ]
                        print(res)
                        yield [
                            b'%' + opt + ml + p +lm + b's',
                            v
                        ]
                for v in us_vals:
                    yield [
                        b'%' + opt + ml + p + b'ls',
                        v
                    ]
    
    
cmp_us_cases = []

cmp_p_cases = []

cmp_d_cases = []

cmp_ud_cases = []

cmp_i_cases = []

cmp_o_cases = []

cmp_uo_cases = []

cmp_x_cases = []

cmp_ux_cases = []

cmp_u_cases = []

cmp_uu_cases = []

cmp_sets = [
    {
        'name' : 'raw cases',
        'cases' : cmp_raw_cases,
    },
    {
        'name' : 'percent cases',
        'cases' : cmp_percent_cases,
    },
    {
        'name' : 'c conv specifier cases',
        'cases' : cmp_c_cases,
    },
    {
        'name' : 'C conv specifier cases',
        'cases' : cmp_uc_cases,
    },
    {
        'name' : 's conv specifier cases',
        'cases' : cmp_s_cases(),
    },
    {
        'name' : 'S conv specifier cases',
        'cases' : cmp_us_cases,
    },
    {
        'name' : 'p conv specifier cases',
        'cases' : cmp_p_cases,
    },
    {
        'name' : 'd conv specifier cases',
        'cases' : cmp_d_cases
    },
    {
        'name' : 'D conv specifier cases',
        'cases' : cmp_ud_cases
    },
    {
        'name' : 'i conv specifier cases',
        'cases' : cmp_i_cases
    },
    {
        'name' : 'o conv specifier cases',
        'cases' : cmp_o_cases
    },
    {
        'name' : 'O conv specifier cases',
        'cases' : cmp_uo_cases
    },
    {
        'name' : 'x conv specifier cases',
        'cases' : cmp_x_cases
    },
    {
        'name' : 'X conv specifier cases',
        'cases' : cmp_ux_cases
    },
    {
        'name' : 'u conv specifier cases',
        'cases' : cmp_u_cases
    },
    {
        'name' : 'U conv specifier cases',
        'cases' : cmp_uu_cases
    },
]

segv_set = []

lks_set = []
