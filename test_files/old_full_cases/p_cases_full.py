# -*- coding: utf-8 -*-

from tools.vals import pointer_vals as vals
from tools.factories import generator_comb_factory, subset_comb_generator_factory

test_sets = [
    ('pointer tests', b'p', vals, subset_comb_generator_factory),
]

cases_generator = generator_comb_factory(test_sets)
