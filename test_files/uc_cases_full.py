# -*- coding: utf-8 -*-

from tools.vals import wchar_vals as vals
from tools.powerset import powerset
from tools.elems import min_len, len_mod
from tools.factories import generator_comb_factory, subset_comb_generator_factory

options = [b''.join(list(i)) for i in powerset([b' ', b'+', b'-', b'#'])]

test_sets = [
    ('wide char tests', b'C', vals, subset_comb_generator_factory),
]

cases_generator = generator_comb_factory(test_sets)
