# -*- coding: utf-8 -*-

from tools.vals import pos_num_vals as vals
from tools.factories import generator_comb_factory

test_sets = [
    ('x tests', b'x', vals),
]

cases_generator = generator_comb_factory(test_sets)
