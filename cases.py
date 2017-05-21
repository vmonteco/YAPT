#!/usr/bin/env python3
# -*- coding: utf-8 -*-

options = [''] + [i for i in " +#0-"]
min_len = [''] + ['0', '1', '-1', '-10', '10', '100', '-100', 'bar']
precision = [''] + ['0', '1', '-1', '5',  '-10', '10', '100', '-100', 'bar']
len_mod = ['', 'j', 'hh', 'll', 'l', 'h', 'z', 'bar']
conv_spec = [''] + [i for i in "cCsSpdDioOxXuU%a"]
val = [
    None,
    
    b'foo',
    b'bar',
    
]
all_cases = 

sets = [
    {
        'name' : 'test test',
        'cases' : [
            [b'foo',],
            [b'far',],
        ]
    },
    {
        'name' : 'test test bis',
        'cases' : [
            [b'foo'],
            [b'far'],
        ]
    },
    
]

segv_cases = [
    []
    for i in
]

undef_cases = [

]

leak_cases = [

]
