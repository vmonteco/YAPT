#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tools.factories import generator_comb_factory
import test_files.full_cases.percent_cases_full as percent_cases
import test_files.full_cases.c_cases_full as c_cases
import test_files.full_cases.s_cases_full as s_cases
import test_files.full_cases.p_cases_full as p_cases
import test_files.full_cases.d_cases_full as d_cases
import test_files.full_cases.i_cases_full as i_cases
import test_files.full_cases.o_cases_full as o_cases
import test_files.full_cases.x_cases_full as x_cases
import test_files.full_cases.ux_cases_full as ux_cases
import test_files.full_cases.u_cases_full as u_cases

test_sets = (
    percent_cases.test_sets
    + c_cases.test_sets
    + s_cases.test_sets
    + p_cases.test_sets
    + d_cases.test_sets
    + i_cases.test_sets
    + o_cases.test_sets
    + x_cases.test_sets
    + ux_cases.test_sets
    + u_cases.test_sets
)

cases_generator = generator_comb_factory(test_sets)
