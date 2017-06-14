# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import test_files.percent_cases_regular as percent_cases

test_sets = percent_cases.test_sets

cases_generator = generator_factory(test_sets)
