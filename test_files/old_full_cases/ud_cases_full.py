# -*- coding: utf-8 -*-

from tools.vals import pos_num_vals, neg_num_vals
from tools.factories import generator_comb_factory, subset_comb_generator_factory

test_sets = [
    ('D tests', b'D', pos_num_vals + neg_num_vals, subset_comb_generator_factory),
]

cases_generator = generator_comb_factory(test_sets)
