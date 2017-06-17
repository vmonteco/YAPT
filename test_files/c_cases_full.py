# -*- coding: utf-8 -*-

from tools.vals import char_vals as vals
from tools.elems import options, min_len, len_mod
from tools.factories import generator_comb_factory

def c_subset_comb_generator_factory(subset):
    yield from ([b''.join([b'%', opt, ml, lm, subset[1], b'\n']), *v]
                for opt in options
                for ml in min_len
                for lm in len_mod
                for v in subset[2]
    )

test_sets = [
    ('char tests', b'c', vals, c_subset_comb_generator_factory),
]

cases_generator = generator_comb_factory(test_sets)
