# `ft_printf_test` :

## Test suite for comparison between an homemade C printf (aka. `ft_printf` for duoquadragintians) and OSX's printf.

### Introduction :

This test suite is a dummy test set intended to help 42 students (and hopefully other people) to realize their own printf.

### How to use :

A Makefile is provided, after adding some path informations (for ft_printf to test and possible libft) :

1. To just compile the test library `libtestftprintf` (Beware : Long compilating time) :

    make
	
2. To compile the library and the executable `testprintf` :

    make testprintf
	
3. To compile and launch the tests :

    make test
	
4. To compile and launch the tests in verbose mode (It will run the executable and display EVERY test output, even the successful ones) :

	make vtest


### What do these tests test and how :

These tests run the two functions to compare in child processes, both the return value and the output on stdout are piped to the parent process and compared. If a difference appears in either the return values or the outputs, the test is considered as failed.

+. It will also display summaries for each handled conv specifier, and a global summary of passed tests at the end, expressed as ratios.

+. If a child process failed for some reason (for instance : segmentation fault), a simple error message is displayed (the test isn't considered as failed if both tested functions failed the same way).

+. This test suite basically tests every case `gcc` accepts with the flags `-Wall -Werror -Wextra` at compiling on OSX.
   So it may also includes undefined behaviours, it also may not compile on other systems.

+. So far, *13943* tests cases are tried. But if you think I've forgotten some, feel free to add your owns.

+. As previously stated, it does *not* test cases that aren't accepted by gcc on OSX.

### NB :

+. This test suite is meant to help students to realize the `ft_printf` project, not to permit them to make a "this-test-suite-fails-so-the-project-doesn't-work-so-here-is-your-0-bye-bye" correction :

   As previously stated, this test suite includes undefined behaviours, check that a found error is a real erro   r before considering the project as failed. (Also, discuss the project, or you're a disgrace as an examiner).

+. */!\ This is a long test suite to compile : ~20min with every test /!\*

   However, it's designed as a library to permit you to test again without having to recompile the whole thing.
   But keep in mind that the whole tests will have to recompile if you adjust the test sets to run by commenting/uncommenting preprocessor directives in `ft_printf_test()` function.

### What improvement could be made :

+. Adapting used tests to the current OS.

+. More explicit error messages in case of child process failure.

+. More tests (if some are forgotten).

+. A specific way to mark undefined behaviours as undefined behaviour in output (And, therefore, sorting out tests by "defined" and "undefined" behaviour).
