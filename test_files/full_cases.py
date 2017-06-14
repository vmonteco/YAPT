#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tools.factories import generator_factory
import test_files.percent_cases as percent_cases
import test_files.c_cases as c_cases

test_sets = (
    percent_cases.test_sets
    + c_cases.test_sets
)

cases_generator = generator_factory(test_sets)

# from limits import *
# import percent_cases
# import c_cases
# import uc_cases
# import s_cases

# sets_set = [
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
