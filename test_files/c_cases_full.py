# -*- coding: utf-8 -*-

from tools.vals import char_vals as vals
from tools.factories import generator_factory

test_sets = [
    ('char tests', b'c', vals),
]

cases_generator = generator_factory(test_sets)
