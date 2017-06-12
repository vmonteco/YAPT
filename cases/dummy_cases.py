#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ctypes

foo_cases = [
    (b'foo\n',),
    (b'This is a test with an int : %d\n', ctypes.c_int(42))
]

bar_cases = [
    (b'bar\n',),
    (b'This is a case with a pointer : %p\n', None)
]
        
dumb_cases = [
    {
        'name': 'foo',
        'cases': foo_cases
    },
    {
        'name': 'bar',
        'cases': bar_cases
    },    
]

def cases_generator():
    return dumb_cases
