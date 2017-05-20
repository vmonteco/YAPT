#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import argparse
import ctypes
import ctypes.util

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# **************************************************************************** #
#                        Retrieving functions to compare.                      #
# **************************************************************************** #

libftprintf = ctypes.cdll.LoadLibrary(os.path.join(BASE_DIR, 'libftprintf.so'))
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
        self.counters = {
            "global_success" : 0,
            "global_tried" : 0,
            "local_success" : 0,
            "local_tried" : 0,
        }

    def run(self, verbose=False, color=True):
        print(messages('welcome'))

    def run_cmp_case(self, case):
        result = {
            'f1_status' : None,
            'f2_status' : None,
            'f1_return' : None,
            'f2_return' : None,
            'f1_output' : None,
            'f2_output' : None
        }
        pipes = {}
        pipes['output_r'], pipes['output_w'] = os.pipe()
        pipes['return_r'], pipes['return_w'] = os.pipe()
        pid = os.fork()
        if (pid == 0):
            os.close(pipes['output_r'])
            os.close(pipes['return_r'])
            os.dup2(pipes['output_w'], sys.stdout.fileno())
            retfd = os.fdopen(pipes['return_w'], 'w')
            ret = self.f1(b'child')
            retfd.write(str(ret))
            retfd.close()
            os.close(pipes['output_w'])
            sys.exit()
        elif pid > 0:
            os.close(pipes['output_w'])
            os.close(pipes['return_w'])
            output_in = os.fdopen(pipes['output_r'])
            return_in = os.fdopen(pipes['return_r'])
            output = output_in.read()
            ret = int(return_in.read())
            status = os.waitpid(pid, 0)
            print('test1 :')
            print("output : %r, return : %s, status : %d" % (output, ret, status[1]))
            output_in.close()
            return_in.close()
        pipes['output_r'], pipes['output_w'] = os.pipe()
        pipes['return_r'], pipes['return_w'] = os.pipe()
        pid = os.fork()
        if (pid == 0):
            os.close(pipes['output_r'])
            os.close(pipes['return_r'])
            os.dup2(pipes['output_w'], sys.stdout.fileno())
            retfd = os.fdopen(pipes['return_w'], 'w')
            ret = self.f2(b'child')
            retfd.write(str(ret))
            retfd.close()
            os.close(pipes['output_w'])
            sys.exit()
        elif pid > 0:
            os.close(pipes['output_w'])
            os.close(pipes['return_w'])
            output_in = os.fdopen(pipes['output_r'])
            return_in = os.fdopen(pipes['return_r'])
            output = output_in.read()
            ret = int(return_in.read())
            status = os.waitpid(pid, 0)
            print('test2 :')
            print("output : %r, return : %s, status : %d" % (output, ret, status[1]))
            output_in.close()
            return_in.close()
        
        

# **************************************************************************** #
        
if __name__ == '__main__':
    t = Tester()
    t.run_cmp_case(b'foo')
    #ft_printf(b"foo\n")
    #printf(b"foo\n")

