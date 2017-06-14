# -*- coding: utf-8 -*-

from tools.vals import wstr_vals as vals
from tools.factories import generator_comb_factory

test_sets = [
    ('wide chars string tests', b'S', vals),
]

cases_generator = generator_comb_factory(test_sets)
