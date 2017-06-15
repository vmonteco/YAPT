# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import test_files.percent_cases_regular as percent_cases
import test_files.c_cases_regular as c_cases
import test_files.uc_cases_regular as uc_cases
import test_files.s_cases_regular as s_cases
import test_files.us_cases_regular as us_cases

test_sets = (
    percent_cases.test_sets
    + c_cases.test_sets
    + uc_cases.test_sets
    + s_cases.test_sets
    + us_cases.test_sets
    + p_cases.test_sets
    + d_cases.test_sets
    + ud_cases.test_sets
    + i_cases.test_sets
    + o_cases.test_sets
    + uo_cases.test_sets#
    + u_cases.test_sets#
    + uu_cases.test_sets#
    + x_cases.test_sets#
    + ux_cases.test_sets#
)


cases_generator = generator_factory(test_sets)
