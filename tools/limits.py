# -*- coding: utf-8 -*-

import ctypes

SHRT_MIN = -ctypes.c_ushort(-1).value // 2
SHRT_MAX = ctypes.c_ushort(-1).value // 2
USHRT_MAX = ctypes.c_ushort(-1).value
CHAR_MIN = -ctypes.c_ubyte(-1).value // 2
CHAR_MAX = ctypes.c_ubyte(-1).value // 2
UCHAR_MAX = ctypes.c_ubyte(-1).value
INT_MIN = -ctypes.c_uint(-1).value // 2
INT_MAX = ctypes.c_uint(-1).value // 2
UINT_MAX = ctypes.c_uint(-1).value
LONG_MIN = -ctypes.c_ulong(-1).value // 2
LONG_MAX = ctypes.c_ulong(-1).value // 2
ULONG_MAX = ctypes.c_ulong(-1).value
LLONG_MIN = -ctypes.c_ulonglong(-1).value // 2
LLONG_MAX = ctypes.c_ulonglong(-1).value // 2
ULLONG_MAX = ctypes.c_ulonglong(-1).value
