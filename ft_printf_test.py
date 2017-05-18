#!/usr/bin/env python3
# -*- codinf: utf-8 -*-

import os, sys
import argparse
import ctypes
import ctypes.util


# **************************************************************************** #
#                        Retrieving functions to compare.                      #
# **************************************************************************** #

libftprintf = ctypes.cdll.LoadLibrary('libftprintf.so')
libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))

ft_printf = libftprintf.printf
printf = libc.printf


# **************************************************************************** #
#                               Defining colors.                               #
# **************************************************************************** #

def colored(s, colored):
    return (s if colored else '')

colors = {
    'red' : colored('', True),
    'cyan' : colored('', True),
    'blue' : colored('', True),
    'prpl' : colored('', True),
    'grn' : colored('', True),
    'yllw' : colored('', True),
    'rst' : colored('', True),
}

colors['succ'] = colors['grn']
colors['fail'] = colors['red']
colors['case'] = colors['prpl']
colors['ntrl'] = colors['yllw']

def colorize(s, res):
    return (s.format(**((colors.update(res)))))

# **************************************************************************** #
#                                Defining texts.                               #
# **************************************************************************** #

msgs = {
    'welcome' : '{grn}Welcome to this ft_printf test programm!{rst}',
    'test_normal_res' : (
        '[{case}%r{rst}] -> [printf/ft_printf]'
        '[{green}%d{rst}/{res1}%d{rst}][{grn}%r{rst}/{res2}%r{rst}].'
    ),
    'test_err' : (
        '[{case}%r{rst}] -> [printf/ft_printf]'
        '[{res1}%d{rst}/{res2}%d{rst}] ({red}%s{rst}).'
    )
}
            
            
# **************************************************************************** #
#                            Defining Tester class.                            #
# **************************************************************************** #

class Tester:

    msgs = msgs

    def __init__(self, f1=printf, f2=ft_printf):
        self.f1 = f1
        self.f2 = f2

    def run(self, verbose=False, color=True):
        print(messages('welcome'))

    def run_case(self, case):
        pipes = os.pipe()
        pid = os.fork()
        if (pid == 0):
            print('child')
            exit()
        else:
            print('parent')
        
        

# **************************************************************************** #
        
if __name__ == '__main__':
    t = Tester()
    t.run_case('foo')
    ft_printf(b"foo\n")
    printf(b"foo\n")

