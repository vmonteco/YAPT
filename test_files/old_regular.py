# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import test_files.old_regular_cases.percent_cases_regular as percent_cases
import test_files.old_regular_cases.c_cases_regular as c_cases
import test_files.old_regular_cases.uc_cases_regular as uc_cases
import test_files.old_regular_cases.s_cases_regular as s_cases
import test_files.old_regular_cases.us_cases_regular as us_cases
import test_files.old_regular_cases.p_cases_regular as p_cases
import test_files.old_regular_cases.d_cases_regular as d_cases
import test_files.old_regular_cases.ud_cases_regular as ud_cases
import test_files.old_regular_cases.i_cases_regular as i_cases
import test_files.old_regular_cases.o_cases_regular as o_cases
import test_files.old_regular_cases.uo_cases_regular as uo_cases
import test_files.old_regular_cases.u_cases_regular as u_cases
import test_files.old_regular_cases.uu_cases_regular as uu_cases
import test_files.old_regular_cases.x_cases_regular as x_cases
import test_files.old_regular_cases.ux_cases_regular as ux_cases
import test_files.old_regular_cases.ux_cases_regular as ux_cases
import test_files.old_regular_cases.misc_regular as misc_cases

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
    + u_cases.test_sets
    + uu_cases.test_sets
    + x_cases.test_sets
    + ux_cases.test_sets
    + misc_cases.test_sets
)


cases_generator = generator_factory(test_sets)
