#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tools.factories import generator_factory
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

cases_generator = generator_factory(test_sets)
#     # (<name>, <conv_spec>, [<val_set keys>, ...]),
#     ('percent tests', b'%', [None]),
#     ('char tests', b'c', c_cases),
#     ('wide char tests', b'C', wchar_vals),
#     ('string tests', b's', str_vals),
#     ('wide char string tests', b'S', wstr_vals),
#     ('pointer tests', b'p', pointer_vals),
#     ('d tests', b'd', pos_num_vals + neg_num_vals),
#     ('D tests', b'D', pos_num_vals + neg_num_vals),
#     ('i tests', b'i', pos_num_vals + neg_num_vals),
#     ('o tests', b'o', pos_num_vals),
#     ('O tests', b'O', pos_num_vals),
#     ('x tests', b'x', pos_num_vals),
#     ('X tests', b'X', pos_num_vals),
#     ('u tests', b'u', pos_num_vals),
#     ('U tests', b'U', pos_num_vals),
# ]

# def cases_generator():

#     for s in sets_set:

#         def f():
#             for ml in min_len:
#                 for p in precision:
#                     for lm in len_mod:
#                         for v in s[2]:
#                             for opt in options:
#                                 yield([b''.join([b'%', opt, ml, p, lm, s[1], b'\n']), v])

#         yield({
#             'name' : s[0],
#             'cases' : f(),
#         })
