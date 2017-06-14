#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import ctypes
import ctypes.util
import imp
import importlib
import signal
import time
import subprocess

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

class Timeout:

    """
    Context manager to handle operations taking to long time.
    Raises a TimeoutError in such case (that would have to be handled by a
    try/except block).
    """
    
    def __init__(self, t=1, msg='This operation took too long'):
        self.t = t
        self.error_msg = msg

    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_msg)

    def __enter__(self):
        if self.t != 0:
            signal.signal(signal.SIGALRM, self.handle_timeout)
            signal.setitimer(signal.ITIMER_REAL, self.t)
            #signal.alarm(self.t)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)
        
def timeout_handler(fd):
    fd.write(str(-1))
    sys.exit(1)
        
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
        '[case: #%s][{case}%r{rst}] -> [%s/%s]'
        '[{grn}%d{rst}/{res1}%d{rst}][{grn}%r{rst}/{res2}%r{rst}].'
    ),
    'test_err': (
        '[case: #%s][{case}%r{rst}] -> [%s/%s]'
        '[{res1}%s{rst}/{res2}%s{rst}] ({res}%s{rst}).'
    ),
    'exit_err': '{fail}%s cases exited non zero statuses.{rst}'
}

# *************************************************************************** #
#                            Defining Tester class.                           #
# *************************************************************************** #


class Tester:

    msgs = msgs

    def __init__(self, f1=printf, f2=ft_printf):
        self.f1 = f1
        self.f2 = f2  # function to test
        self.counters = {
            'global_success': 0,
            'global_tried': 0,
            'local_success': 0,
            'local_tried': 0,
            'global_exit_err': 0,
            'local_exit_err': 0,
        }

    def run(self, cases_generator=None, verbose=False, quiet=False,
            timeout=0.15):
        """
        This is the main run() method. It will (or not) trigger other
        run submethods.
        """
        print(colorize(self.msgs['welcome']))
        self.run_cmp_cases(cases_generator(), verbose=verbose, quiet=quiet,
                           timeout=timeout)
        if self.counters['global_exit_err'] == 0:
            print('Running cases in current process...')
            cases = cases_generator()
            for s in cases:
                for c in s['cases']:
                    self.f2(*s)
            l = subprocess.call(['leaks', str(os.getpid())])
            if l == 0:
                print(colorize('{succ}No leaks found.{rst}'))
            elif l > 1:
                print(colorize('{fail}An error occured with leaks.{rst}'))
            else:
                print(colorize('{fail}Leaks found.{rst}'))
        else:
            print(colorize(
                (
                    '\n{red}Some subprocesses failed (non 0 exit statuses)'
                    'Leaks tests failed.{rst}\n'
                )))

    def run_cmp_cases(self, cases, verbose=False, quiet=False, debug=False,
                      timeout=0.15):
        """
        This run submethod just run test sets by calling run_in_subprocess().
        """
        self.counters['global_tried'] = 0
        self.counters['global_success'] = 0
        for case in cases:
            self.run_cmp_cases_subsets(case['name'], case, verbose=verbose,
                                       quiet=quiet, timeout=timeout)
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
        if (self.counters['local_exit_err'] != 0):
            print(colorize(self.msgs['exit_err'])
                  % (
                      self.counters['local_exit_err']
                  ))

    def run_cmp_cases_subsets(self, name, cases, verbose=False, quiet=False,
                              timeout=0.15):
        """
        This run submethod just run test subsets by calling
        run_in_subprocess().
        """
        self.counters['local_tried'] = 0
        self.counters['local_success'] = 0
        self.counters['local_exit_err'] = 0
        print(colorize(self.msgs['subset_head'], {}) % (cases['name'],))
        for case in cases['cases']:
            self.run_cmp_case(name, case, verbose=verbose, quiet=quiet,
                              timeout=timeout)
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
            if (self.counters['local_exit_err'] != 0):
                print(colorize(self.msgs['exit_err'])
                      % (
                          self.counters['local_exit_err']
                      ))

                
    def run_cmp_case(self, name, case, verbose=False, quiet=False,
                     timeout=0.15):
        """
        This method just runs an actual test by calling
        run_in_subprocess().
        """
        res = {
            'f1': self.run_in_fork(self.f1, case, timeout=timeout),
            'f2': self.run_in_fork(self.f2, case, timeout=timeout)
        }
        self.interpret_cmp_results(case, res, verbose, quiet)
        print('results : local (%s) : [%s/%s], global : [%s/%s]' % (
            name,
            self.counters['local_success'],
            self.counters['local_tried'],
            self.counters['global_success'],
            self.counters['global_tried']
        ), end='\r')

                
    def run_in_fork(self, function, case, timeout=0.15):
        """
        This method runs a test case by passing it to both f1 and f2,
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
            try:
                with Timeout(t=5) as t:
                    os.close(pipes['output_r'])
                    os.close(pipes['return_r'])
                    os.dup2(pipes['output_w'], sys.stdout.fileno())
                    return_fd = os.fdopen(pipes['return_w'], 'w')
                    #signal.signal(signal.SIGTERM, lambda s, f: handle_timeout(return_fd))
                    ret = function(*case)
            except TimeoutError as e:
                pass
            finally:
                os.close(pipes['output_w'])
                return_fd.write(str(ret))
                return_fd.close()
                sys.exit()
        else:
            res = {}
            res['status'] = 'timeout'
            os.close(pipes['output_w'])
            os.close(pipes['return_w'])
            # output_in = os.fdopen(pipes['output_r'], encoding='cp1252')
            output_in = os.fdopen(pipes['output_r'], mode='rb')#, encoding='utf8')
            return_in = os.fdopen(pipes['return_r'])
            try:
                with Timeout(t=timeout) as t:
                    res['output'] = output_in.read()
                    res['return'] = int(return_in.read())
                    res['status'] = os.waitpid(pid, 0)[1]
            except TimeoutError as e:
                os.kill(pid, signal.SIGTERM)
                os.waitpid(pid, 0)
            finally:
                output_in.close()
                return_in.close()
            return res


        
    def interpret_cmp_results(self, case, res, verbose=False, quiet=False):
        """
        This method manges the display of the results for comparison tests.
        It also stores the success/failure to count it in the final ratio.
        """
        self.counters['local_tried'] += 1
        self.counters['global_tried'] += 1
        cols = {}
        m = None
        if res['f2']['status'] != 0:
            self.counters['global_exit_err'] += 1
            self.counters['local_exit_err'] += 1
        if (res['f1']['status'] == 0 and res['f2']['status'] == 0):
            out_ok = (res['f1']['output'] == res['f2']['output'])
            ret_ok = (res['f1']['return'] == res['f2']['return'])
            cols['res2'] = colors['succ'] if out_ok else colors['fail']
            cols['res1'] = colors['succ'] if ret_ok else colors['fail']
            if ret_ok and out_ok:
                self.counters['local_success'] += 1
                self.counters['global_success'] += 1
            if (not (ret_ok and out_ok)) or verbose and not quiet:
                m = (colorize(self.msgs['test_normal_res'], cols)
                     % (
                         self.counters['global_tried'],
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
                     self.counters['global_tried'],
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
                     self.counters['global_tried'],
                     ', '.join([str(i) for i in case]),
                     self.f1.__name__,
                     self.f2.__name__,
                     res['f1']['status'],
                     res['f2']['status'],
                     'different exit statuses.'
                 ))
        if m and not quiet:
            print(m)

# *************************************************************************** #

if __name__ == '__main__':

    # *********************************************************************** #
    #                       Argument parser definition                        #
    # *********************************************************************** #

    parser = argparse.ArgumentParser(
        description='This is a ft_printf python testing tool.')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='this option enables successful results display.')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help=('this option disables any case results display.'
                              'It permits to have a short yet global view on '
                              'every test set result'))
    parser.add_argument('-u', '--uncolored', dest='colors',
                        action='store_false', help='disable colors.')
    parser.add_argument('-t', '--timeout', dest='t',
                         type=float, default=0.25,
                        help=(
                            'Set timeout duration. 0 will disable short '
                            'timeout (but a default 5 seconds timeout is still'
                            ' activated to clean any non-terminated'
                            ' subprocess if the parent process can\'t kill'
                            'it in case of timeout).'
                        ))
    parser.add_argument('filename',
                        help=(
                            'A valid python3 file containing a generator '
                            'called "cases_generator". This iterable will '
                            'contain several case sets that will be '
                            'dictionnaries. These dictionaries will have a'
                            '\'name\' entry to describe the cases subset, and'
                            ' a \'cases\' entry '
                        ))
    args = parser.parse_args()

    # *********************************************************************** #
    #                           importing cases                               #
    # *********************************************************************** #

    dir = os.path.dirname(os.path.abspath(args.filename))
    f = os.path.basename(os.path.abspath(args.filename))
    mod = imp.find_module(os.path.splitext(f)[0], [dir])
    if mod:
        try:
            m = imp.load_module('cases', *mod)
        finally:
            mod[0].close()
        cases_generator = m.cases_generator

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

    print(args)
    t = Tester()
    t.run(cases_generator=cases_generator,
          verbose=args.verbose, quiet=args.quiet, timeout=args.t)
