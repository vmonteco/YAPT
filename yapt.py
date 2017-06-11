#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import ctypes
import ctypes.util
import cases

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# *************************************************************************** #
#                        Retrieving functions to compare.                     #
# *************************************************************************** #

libftprintf = ctypes.cdll.LoadLibrary(os.path.join(BASE_DIR, 'libftprintf.so'))
libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))

ft_printf = libftprintf.ft_printf
printf = libc.printf


# *************************************************************************** #
#                                Defining texts.                              #
# *************************************************************************** #

msgs = {
    'welcome': '{yllw}Welcome to this ft_printf testing tool!{rst}',
    'global_head': '{grn}Welcome to this ft_printf test programm!{rst}',
    'global_res': '{res}Global{rst} : [{res}%d{rst}/{grn}%d{rst}]',
    'segv_res': '{res}Segv tests passed{rst} : [{res}%d{rst}/{grn}%d{rst}]',
    'segv_case_res': '[{case}%r{rst}] -> [status : {res}%s{rst}]',
    'subset_head': '*** Running "{grn}%s{rst}" tests. ***',
    'subset_res':
    '--- {res}%s{rst} results : [{res}%d{rst}/{grn}%d{rst}]. ---',
    'test_normal_res': (
        '[{case}%r{rst}] -> [%s/%s]'
        '[{grn}%d{rst}/{res1}%d{rst}][{grn}%r{rst}/{res2}%r{rst}].'
    ),
    'test_err': (
        '[{case}%r{rst}] -> [%s/%s]'
        '[{res1}%d{rst}/{res2}%d{rst}] ({res}%s{rst}).'
    )
}

# *************************************************************************** #
#                            Defining Tester class.                           #
# *************************************************************************** #


class Tester:

    msgs = msgs

    def __init__(self, f1=printf, f2=ft_printf):
        self.f1 = f1
        self.f2 = f2
        self.counters = {
            "global_success": 0,
            "global_tried": 0,
            "local_success": 0,
            "local_tried": 0,
        }

    def run(self, cmp_sets=None, segv_set=None, lks_set=None, verbose=False,
            quiet=False):
        """
        This is the main run() method. It will (or not) trigger other
        run submethods.
        """
        print(colorize(self.msgs['welcome']))
        if cmp_sets:
            self.run_cmp_cases(cmp_sets, verbose, quiet)
        if segv_set:
            self.run_segv_cases(segv_set, verbose, quiet)
        if lks_set:
            self.run_lks_cases(lks_set, verbose, quiet)

    def run_in_subprocess(self, function, case):
        """
        This method run a test case by passing it to both f1 and f2,
        and by running it in subprocesses.
        It monitors the output on STDOUT, the function's return and the
        child process exit status..
        """
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
            output_in = os.fdopen(pipes['output_r'], encoding='cp1252')
            return_in = os.fdopen(pipes['return_r'])
            res['output'] = output_in.read()
            res['return'] = int(return_in.read())
            res['status'] = os.waitpid(pid, 0)[1]
            return res

    def run_cmp_cases(self, cases, verbose=False, quiet=False):
        """
        This run submethod just run test sets by calling run_in_subprocess().
        """
        self.counters['global_tried'] = 0
        self.counters['global_success'] = 0
        for case in cases:
            self.run_cmp_cases_subsets(case, verbose, quiet)
        if self.counters['global_tried'] > 0:
            success = self.counters['global_tried'] == self.counters[
                'global_success'
            ]
            col = colors['succ'] if success else colors['fail']
            print(
                colorize(self.msgs['global_res'], {'res': col})
                % (
                    self.counters['global_success'],
                    self.counters['global_tried'],
                )
            )

    def run_cmp_cases_subsets(self, cases, verbose=False, quiet=False):
        """
        This run submethod just run test subsets by calling
        run_in_subprocess().
        """
        self.counters['local_tried'] = 0
        self.counters['local_success'] = 0
        print(colorize(self.msgs['subset_head'], {}) % (cases['name'],))
        for case in cases['cases']:
            self.run_cmp_case(case, verbose, quiet)
        if self.counters['local_tried'] > 0:
            success = (
                self.counters['local_tried'] == self.counters['local_success']
            )
            col = colors['succ'] if success else colors['fail']
            print(colorize(self.msgs['subset_res'], {'res': col})
                  % (
                      cases['name'],
                      self.counters['local_success'],
                      self.counters['local_tried']
                  ))

    def run_cmp_case(self, case, verbose=False, quiet=False):
        """
        This method just runs an actual test by calling
        run_in_subprocess().
        """
        res = {
            'f1': self.run_in_subprocess(self.f1, case),
            'f2': self.run_in_subprocess(self.f2, case),
        }
        self.interpret_cmp_results(case, res, verbose, quiet)

    def interpret_cmp_results(self, case, res, verbose=False, quiet=False):
        """
        This method manges the display of the results for comparison tests.
        It also stores the success/failure to count it in the final ratio.
        """
        cols = {}
        m = None
        if (res['f1']['status'] == 0 and res['f2']['status'] == 0):
            out_ok = (res['f1']['output'] == res['f2']['output'])
            ret_ok = (res['f1']['return'] == res['f2']['return'])
            cols['res2'] = colors['succ'] if out_ok else colors['fail']
            cols['res1'] = colors['succ'] if ret_ok else colors['fail']
            if ret_ok and out_ok:
                self.counters['local_success'] += 1
                self.counters['global_success'] += 1
            self.counters['local_tried'] += 1
            self.counters['global_tried'] += 1
            if (not (ret_ok and out_ok)) or verbose and not quiet:
                m = (colorize(self.msgs['test_normal_res'], cols)
                     % (
                         ', '.join([str(i) for i in case]),
                         self.f1.__name__,
                         self.f2.__name__,
                         res['f1']['return'],
                         res['f2']['return'],
                         res['f1']['output'],
                         res['f2']['output']
                     ))
        elif (res['f1']['status'] == res['f2']['status']):
            cols['res1'] = colors['succ']
            cols['res2'] = colors['succ']
            cols['res'] = colors['ntrl']
            m = (colorize(self.msgs['test_err'], cols)
                 % (
                     ', '.join([str(i) for i in case]),
                     self.f1.__name__,
                     self.f2.__name__,
                     res['f1']['status'],
                     res['f2']['status'],
                     'error on both case.'
                 ))
        else:
            cols['res1'] = colors['succ']
            cols['res2'] = colors['fail']
            cols['res'] = colors['fail']
            m = (colorize(self.msgs['test_err'], cols)
                 % (
                     ', '.join([str(i) for i in case]),
                     self.f1.__name__,
                     self.f2.__name__,
                     res['f1']['status'],
                     res['f2']['status'],
                     'different exit statuses.'
                 ))
        if m and not quiet:
            print(m)

    def run_segv_cases(self, cases, verbose=False, quiet=False):
        self.counters['global_tried'] = 0
        self.counters['global_success'] = 0
        for case in cases:
            res = self.run_in_subprocess(self.f2, case)
            self.interpret_segv_result(res, case, verbose)
        self.print_segv_cases_result()

    def interpret_segv_result(self, result, case, verbose=False, quiet=False):
        self.counters['global_tried'] += 1
        if result['status'] == 0:
            self.counters['global_success'] += 1
        if result['status'] != 0 or verbose:
            res = colors['succ'] if result['status'] == 0 else colors['fail']
            print(
                colorize(self.msgs['segv_case_res'], {'res': res})
                % (
                    case,
                    result['status']
                )
            )

    def print_segv_cases_result(self):
        succ = (
            self.counters['global_tried'] == self.counters['global_success']
        )
        res = colors['succ'] if succ else colors['fail']
        print(
            colorize(self.msgs['segv_res'], {'res': res})
            % (
                self.counters['global_success'],
                self.counters['global_tried']
            ))

    def run_lks_cases(self, cases, verbose=False, quiet=False):
        print("Running cases to test leaks.")
        for case in cases:
            self.f2(*case)


# *************************************************************************** #

if __name__ == '__main__':

    # *********************************************************************** #
    #                       Argument parser definition                        #
    # *********************************************************************** #

    parser = argparse.ArgumentParser(
        description='This is a ft_printf python testing tool.',
        epilog=(
            'NB : If none of -c, -s, or -a args is passed to this tool, '
            'every test sets is run in the following order : comparison, segv,'
            ' leaks.'
        ))
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='this option enables successful results display.')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help=('this option disables any case results display.'
                              'It permits to have a short yet global view on '
                              'every test set result'))
    parser.add_argument('-u', '--uncolored', dest='colors',
                        action='store_false', help='disable colors.')
    parser.add_argument('-c', '--cmp', action='store_true',
                        help='Enable comparison tests. It will run every case '
                        'in a child process.')
    parser.add_argument('-s', '--segv', action='store_true',
                        help=(
                            'Enable segmentation fault and other status errors'
                            ' tests.'
                            ' It will run every case in a child process.'
                        ))
    parser.add_argument('-a', '--all', action='store_true',
                        help='Enable all (comparison+segfault+leaks) tests.')
    parser.add_argument('-l', '--leaks', action='store_true',
                        help=(
                            'Enable leaks tests, it will run every case '
                            'in the current process, then run an infinite loop'
                            ' so you can run leaks. '
                            'You\'ll have to ctrl+C to close the programm.'
                            '\n/!\ If an error occurs, it won\'t be handled.'
                            '/!\.'
                        ))
    args = parser.parse_args()

    # *********************************************************************** #
    #                           Colors definition                             #
    # *********************************************************************** #

    def colored(s):
        return (s if args.colors else '')

    colors = {
        'red': colored('\033[91m'),
        'cyan': colored('\033[96m'),
        'blue': colored('\033[94m'),
        'prpl': colored('\033[95m'),
        'grn': colored('\033[92m'),
        'yllw': colored('\033[93m'),
        'rst': colored('\033[0m'),
    }

    colors['succ'] = colors['grn']
    colors['fail'] = colors['red']
    colors['case'] = colors['prpl']
    colors['ntrl'] = colors['yllw']

    def colorize(s, res={}):
        cols = colors
        cols.update(res)
        return (s.format(**cols))

    # *********************************************************************** #
    #                           Test sets defintion                           #
    # *********************************************************************** #

    all_tests = not (args.cmp or args.leaks or args.segv)
    cmp_sets = cases.cmp_sets if args.cmp or all_tests else None
    segv_set = cases.segv_set if args.segv or all_tests else None
    lks_set = cases.lks_set if args.leaks or all_tests else None

    t = Tester()
    t.run(cmp_sets=cmp_sets, segv_set=segv_set, lks_set=lks_set,
          verbose=args.verbose, quiet=args.quiet)
    if (args.leaks or all_tests):
        while (True):
            pass
