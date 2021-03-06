#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tools.factories import generator_comb_factory
import test_files.percent_cases_full as percent_cases
import test_files.c_cases_full as c_cases
import test_files.uc_cases_full as uc_cases
import test_files.s_cases_full as s_cases
import test_files.us_cases_full as us_cases
import test_files.p_cases_full as p_cases
import test_files.d_cases_full as d_cases
import test_files.ud_cases_full as ud_cases
import test_files.i_cases_full as i_cases
import test_files.o_cases_full as o_cases
import test_files.uo_cases_full as uo_cases
import test_files.x_cases_full as x_cases
import test_files.ux_cases_full as ux_cases
import test_files.u_cases_full as u_cases
import test_files.uu_cases_full as uu_cases

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
    + uo_cases.test_sets
    + x_cases.test_sets
    + ux_cases.test_sets
    + u_cases.test_sets
    + uu_cases.test_sets
)

cases_generator = generator_comb_factory(test_sets)
