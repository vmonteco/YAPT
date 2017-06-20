# -*- coding: utf-8 -*-

from tools.vals import wstr_vals as vals
from tools.factories import generator_comb_factory, subset_comb_generator_factory

test_sets = [
    ('wide chars string tests (S)', b'S', vals, subset_comb_generator_factory),
]

cases_generator = generator_comb_factory(test_sets)
