# -*- coding:  utf-8 -*-

from tools.factories import generator_factory

length_cases = [
    [b''.join([b'a' for i in range(4095)])],
]

test_sets = [
    {
        'name': 'lenght test',
        'cases': length_cases
    },
]

cases_generator = generator_factory(test_sets)
