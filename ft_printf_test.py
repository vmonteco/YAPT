#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import argparse
import ctypes
import ctypes.util
import cases

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
    'red' : colored('\033[91m', True),
    'cyan' : colored('\033[96m', True),
    'blue' : colored('\033[94m', True),
    'prpl' : colored('\033[95m', True),
    'grn' : colored('\033[92m', True),
    'yllw' : colored('\033[93m', True),
    'rst' : colored('\033[0m', True),
}

colors['succ'] = colors['grn']
colors['fail'] = colors['red']
colors['case'] = colors['prpl']
colors['ntrl'] = colors['yllw']

def colorize(s, res):
    cols = colors
    cols.update(res)
    return (s.format(**cols))

# **************************************************************************** #
#                                Defining texts.                               #
# **************************************************************************** #

msgs = {
    'global_head' : '{grn}Welcome to this ft_printf test programm!{rst}',
    'global_res' : '{res}Global{rst} : [{res}%d{rst}/{grn}%d{rst}]',
    'subset_head' : '--- Running "{grn}%s{rst}" tests. ---',
    'subset_res' : '*** {res}%s{rst} results : [{res}%d{rst}/{grn}%d{rst}]. ***',

    'test_normal_res' : (
        '[{case}%r{rst}] -> [printf/ft_printf]'
        '[{grn}%d{rst}/{res1}%d{rst}][{grn}%r{rst}/{res2}%r{rst}].'
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

        
    def run_in_subprocess(self, function, case):
        pipes = {}
        pipes['output_r'], pipes['output_w'] = os.pipe()
        pipes['return_r'], pipes['return_w'] = os.pipe()
        pid = os.fork()
        if (pid < 0):
            raise Exception('unable to fork')
        elif (pid == 0):
            os.close(pipes['output_r'])
            os.close(pipes['return_r'])
            os.dup2(pipes['output_w'], sys.stdout.fileno())
            return_fd = os.fdopen(pipes['return_w'], 'w')
            ret = function(*case)
            return_fd.write(str(ret))
            return_fd.close()
            os.close(pipes['output_w'])
            sys.exit()
        else:
            res = {}
            os.close(pipes['output_w'])
            os.close(pipes['return_w'])
            output_in = os.fdopen(pipes['output_r'])
            return_in = os.fdopen(pipes['return_r'])
            res['output'] = output_in.read()
            res['return'] = int(return_in.read())
            res['status'] = os.waitpid(pid, 0)[1]
            return res

    def run_cmp_cases(self, cases):
        self.counters['global_tried'] = 0
        self.counters['global_success'] = 0
        for case in cases:
            self.run_cmp_cases_subsets(case)
        if self.counters['global_tried'] > 0:
            success = self.counters['global_tried'] == self.counters['global_success']
            col = colors['succ'] if success else colors['fail']
            print(
                colorize(self.msgs['global_res'], {'res' : col})
                % (
                    self.counters['global_success'],
                    self.counters['global_tried'],
                )
            )
            
    def run_cmp_cases_subsets(self, cases):
        self.counters['local_tried'] = 0
        self.counters['local_success'] = 0
        print(colorize(self.msgs['subset_head'], {}) % (cases['name'],))
        for case in cases['cases']:
            self.run_cmp_case(case)
        if self.counters['local_tried'] > 0:
            success = (
                self.counters['local_tried'] == self.counters['local_success']
            )
            col = colors['succ'] if success else colors['fail']
            print(colorize(self.msgs['subset_res'], {'res' : col})
                  % (
                      cases['name'],
                      self.counters['local_success'],
                      self.counters['local_tried']
                  )
            )
              
        
    def run_cmp_case(self, case):
        res = {
            'f1' : self.run_in_subprocess(self.f1, case),
            'f2' : self.run_in_subprocess(self.f2, case),
        }
        self.interpret_results(case, res)
        
    def interpret_results(self, case, res):
        cols = {}
        if (res['f1']['status'] == 0 and res['f2']['status'] == 0) :
            out_ok = (res['f1']['output'] == res['f2']['output'])
            ret_ok = (res['f1']['return'] == res['f2']['return'])
            cols['res2'] = colors['succ'] if out_ok else colors['fail']
            cols['res1'] = colors['succ'] if ret_ok else colors['fail']
            if ret_ok and out_ok:
                self.counters['local_success'] += 1
                self.counters['global_success'] += 1
            self.counters['local_tried'] += 1
            self.counters['global_tried'] += 1
            m = (colorize(self.msgs['test_normal_res'], cols)
                 % (
                     ', '.join([str(i) for i in case]),
                     res['f1']['return'],
                     res['f2']['return'],
                     res['f1']['output'],
                     res['f2']['output']
                ))
            print(m)
        else:
            print('error')    
            
# **************************************************************************** #
        
if __name__ == '__main__':
    t = Tester()
    t.run_cmp_cases(cases.sets)
    #ft_printf(b"foo\n")
    #printf(b"foo\n")

