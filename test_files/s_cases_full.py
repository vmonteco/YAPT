# -*- coding: utf-8 -*-

from tools.vals import str_vals, wstr_vals
from tools.elems import len_mod, options, min_len, precision
from tools.factories import generator_comb_factory, subset_comb_generator_factory

def s_subset_comb_generator_factory(subset):
    yield from ([b''.join([b'%', opt, p, ml, lm, subset[1], b'\n']), *v]
                for opt in options
                for p in precision
                for ml in min_len
                for lm in len_mod if lm != b'l' and lm != b'll' and lm != b'j'
                for v in subset[2])

def wide_s_subset_comb_generator_factory(subset):
    yield from ([b''.join([b'%', opt, p, ml, b'l', subset[1], b'\n']), *v]
                for opt in options
                for p in precision
                for ml in min_len
                for v in subset[2])
    
test_sets = [
    ('string tests', b's', str_vals, s_subset_comb_generator_factory),
    ('wide chars string tests', b's', wstr_vals, wide_s_subset_comb_generator_factory),
]

cases_generator = generator_comb_factory(test_sets)
