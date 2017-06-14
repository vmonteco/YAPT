# -*- coding: utf-8 -*-

from tools.factories import generator_comb_factory

test_sets = [
    ('percent tests', b'%', [[]]),
]

cases_generator = generator_comb_factory(test_sets)
