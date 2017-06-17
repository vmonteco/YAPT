# -*- coding: utf-8 -*-

from tools.elems import options, min_len, precision, len_mod

def subset_comb_generator_factory(subset):
    yield from ([b''.join([b'%', opt, ml, p, lm, subset[1], b'\n']), *v]
                for opt in options
                for ml in min_len
                for p in precision
                for lm in len_mod
                for v in subset[2]
    )

def generator_comb_factory(test_sets):
    def f():
        yield from ({'name': s[0], 'cases': s[3](s)} for s in test_sets)
    return f

# def subset_generator_factory(subset):
#     yield from (i for i in subset['cases'])

def generator_factory(test_sets):
    def f():
        yield from (i for i in test_sets)
    return f
