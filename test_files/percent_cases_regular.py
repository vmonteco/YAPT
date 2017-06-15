# -*- coding: utf-8 -*-

from tools.factories import generator_factory

basic_cases = [
    [b'%%\n'],
    [b'% %\n'],
    [b'%-%\n'],
    [b'%+%\n'],
    [b'%#%\n'],
    [b'%0%\n'],
    [b'%3%\n'],
    [b'% 3%\n'],
    [b'%-3%\n'],
    [b'%+3%\n'],
    [b'%#3%\n'],
    [b'%03%\n'],
    [b'%1%\n'],
    [b'%2%\n'],
    [b'%.%\n'],
    [b'%.0%\n'],
    [b'%.-1%\n'],
    [b'%.1%\n'],
    [b'%.2%\n'],
    [b'%.5%\n'],
    [b'%hh%\n'],
]

mixed_cases = [
    [b'%-4%\n'],
    [b'%-.5%\n'],
    [b'%-.%\n'],
    [b'%-.0%\n'],
    [b'%-3.1%\n'],
    [b'%5.-1%\n'],
    [b'%05.-1%\n'],
    [b'%0.-1%\n'],
    [b'%04%\n'],
    [b'%0.5%\n'],
    [b'%0.%\n'],
    [b'%0.0%\n'],
    [b'%03.1%\n'],
    [b'%0-4%\n'],
    [b'%0-.5%\n'],
    [b'%0-.%\n'],
    [b'%0-.0%\n'],
    [b'%0-3.1%\n'],
]

all_opt_cases = [
    [b'%-+0# 10.4hh%\n'],
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
