# -*- coding: utf-8 -*-

from tools.elems import options, min_len, len_mod

test_sets = [
    ('percent tests', b'%', [[]]),
]

def percent_subset_comb_generator_factory(subset):
    yield from ([b''.join([b'%', opt, ml, lm, subset[1], b'\n']), *v]
                for opt in options
                for ml in min_len
                for lm in len_mod
                for v in subset[2]
    )

def generator_percent_comb_factory(test_sets):
    def f():
        yield from ({'name': s[0], 'cases': percent_subset_comb_generator_factory(s)} for s in test_sets)
    return f
        
cases_generator = generator_percent_comb_factory(test_sets)
