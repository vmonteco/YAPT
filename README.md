# Yet Another Printf Tester (YAPT) :

## Test suite for comparison between an homemade C printf (aka. `ft_printf` for duoquadragintians) and OSX's printf written in Python 3.

### Introduction :

This test suite is a dummy test set intended to help 42 students (and hopefully other people) to realize their own printf.

### How to use :

1. Link your project's path to `./ft_printf` in the YAPT directory.

2. Compile with `make`. It should compile your project and create a shared library (.so) in the YAPT directory.
   This library will be used by ctype to call your ft_printf function.
   
3. Then just run the YAPT executable with one of the test files provided (or even your own test file) :

    ./yapt test_files/dummy_cases.py

You can also find informations about YAPT features by running `./yapt -h`.

### How does it work?

The programm forks and runs each case and each function to compare in a subprocess. The output is captured and piped to parent process, just like the return value.
These values are then interpreted and compared. If the subprocess exits with an error, then the exit status is interpreted.

If every exit status was 0, leaks are tested after running every previous case directly in the parent process.

### How are the test files formated :

These Test files are python files (obviously).

These files must be passed as parameters to the YAPT executable.

These files must contain at least a `cases_generator` element. This element must be an iterable (generator, list...) factory. Its return would contain *test subsets*.
Test subsets are dictionnaries formatted as bellow :

    {'name': name, 'cases': cases}

Where *name* is a string containing a description of the subset, and cases an other iterable containing iterables (again) that will contain arguments to pass to the function for a specific case.

These arguments must use the `ctypes` API. See the examples and https://docs.python.org/3.6/library/ctypes.html#fundamental-data-types for more informations. Also strings must be byte strings (`b''`) and not regular python strings ('').

So the `cases_generator` factory return could look like this :

    [
	    {
		    'name': string,
			'cases': [
				[arg1, arg2, arg3, ...],
				...
			]
		},
		...
	]

`./test_files/dummy_cases.py` also contains a good example of how you could build your own tests.

#### What tests are provided?

+. full_cases.py : This test file gathers content from many others full tests that can be passed as well to yapt.py. These tests are generated combinatorially and there are a *lot* of cases.

+. regular_tests.py : Some tests that should be enough to check most of your ft_printf feature (but probably not all). It also gathers other regular test sets.

+. dummy_tests.py : Just a dummy test with 4 cases to check that the programm runs. It can be a first check to do before doing more advanced tests.

### What does the output mean?

There are two kinds of output you can get for a case :

1. The child process exits normally (this does implies s successful test) :

       [case: #<case index>][<case>] -> [printf/ft_printf][<printf return>/<ft_printf return>][b<printf output>/b<ft_printf output>].

2. The child process does not exits normally :

       [case: #<case index>][<case>] -> [printf/ft_printf][<printf exit status or timeout>/<ft_printf exit status or timeout>] (different exit statuses.).

Also note that if you doesn't enable the `-v` parameter, only the error outputs will be displayed. If you enable the `-q` parameter, only the subsets and global summaries are displayed.

### NB :

+. This test suite is meant to help students to realize the `ft_printf` project, not to permit them to make a "this-test-suite-fails-so-the-project-doesn't-work-so-here-is-your-0-bye-bye" correction :

   This test suite includes undefined behaviours, check that a found error is a real error before considering the project as failed. (Also, discuss the project, or you're a disgrace as an examiner).

### Also :

+. This code is distributed under the GPL3 license terms. Feel free to use it, fork it, copy it, share it, improve it, criticize it, reuse it, contribute with a PR, etc.

### What could be improved :

+. More explicit error messages in case of child process failure.

+. Timeout and other errors detailed counting.

+. Multiprocessing.

+. More/other tests.

+. My English fluency.

+. Your pythonic skills.

+. Norminet's manners.
