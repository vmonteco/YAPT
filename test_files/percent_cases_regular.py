# -*- coding: utf-8 -*-

from tools.factories import generator_factory

basic_cases = [
    [b'%%'],
    [b'% %'],
    [b'%-%'],
    [b'%+%'],
    [b'%#%'],
    [b'%0%'],
    [b'%3%'],
    [b'% 3%'],
    [b'%-3%'],
    [b'%+3%'],
    [b'%#3%'],
    [b'%03%'],
    [b'%1%'],
    [b'%2%'],
    [b'%.%'],
    [b'%.0%'],
    [b'%.-1%'],
    [b'%.1%'],
    [b'%.2%'],
    [b'%.5%'],
    [b'%hh%'],
]

mixed_cases = [
    [b'%-4%'],
    [b'%-.5%'],
    [b'%-.%'],
    [b'%-.0%'],
    [b'%-3.1%'],
    [b'%5.-1%'],
    [b'%05.-1%'],
    [b'%0.-1%'],
    [b'%04%'],
    [b'%0.5%'],
    [b'%0.%'],
    [b'%0.0%'],
    [b'%03.1%'],
    [b'%0-4%'],
    [b'%0-.5%'],
    [b'%0-.%'],
    [b'%0-.0%'],
    [b'%0-3.1%'],
]

all_opt_cases = [
    [b'%-+0# 10.4hh%'],
]

test_sets = [
    {
        'name': 'percent regular tests - basics.',
        'cases': basic_cases
    },
    {
        'name': 'percent regular tests - mixed.',
        'cases': mixed_cases
    },
    {
        'name': 'percent regular tests - all options/flags.',
        'cases': all_opt_cases
    }
]

cases_generator = generator_factory(test_sets)
