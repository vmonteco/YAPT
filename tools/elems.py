# -*- coding: utf-8 -*-

from tools.powerset import powerset

options = [b''.join(list(i)) for i in powerset([b' ', b'+', b'-', b'0', b'#'])]
min_len = [b'', b'0', b'1', b'2',  b'10']
precision = [b'.-1', b'.-2', b'', b'.', b'.0', b'.1', b'.2', b'.10']
len_mod = [b'', b'j', b'hh', b'll', b'l', b'h', b'z']

