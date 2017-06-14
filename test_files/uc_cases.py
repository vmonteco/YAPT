# -*- coding: utf-8 -*-

from vals import wchar_vals as vals

test_sets = [
    ('wide char tests', b'c', vals),
]

cases_generator = generator_factory(test_sets)
