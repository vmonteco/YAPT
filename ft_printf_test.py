#!/usr/bin/env python3

import ctypes
import ctypes.util

libftprintf = ctypes.cdll.LoadLibrary('libftprintf.so')
libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))

ft_printf = libftprintf.printf
printf = libc.printf

if __name__ == '__main__':
    ft_printf(b"foo\n")
    printf(b"foo\n")
    
