# -*- coding: utf-8 -*-

from tools.factories import generator_factory

test_sets = [
    ('percent tests', b'%', [[]]),
]

cases_generator = generator_factory(test_sets)
