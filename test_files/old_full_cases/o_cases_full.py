# -*- coding: utf-8 -*-

from tools.vals import pos_num_vals as vals
from tools.factories import generator_comb_factory, subset_comb_generator_factory

test_sets = [
    ('o tests', b'o', vals, subset_comb_generator_factory),
]

cases_generator = generator_comb_factory(test_sets)
