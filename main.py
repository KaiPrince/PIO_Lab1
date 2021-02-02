"""
 * Project Name: PIO_Lab1
 * File Name: main.py
 * Programmer: Kai Prince
 * Date: Tue, Feb 02, 2021
 * Description: This program compares sorting algorithms.
"""
import cProfile
import io
import pstats
from typing import Callable

import numpy
from func_timeout import func_set_timeout
from func_timeout.exceptions import FunctionTimedOut

from bogo_sort import bogo_sort
from bubble_sort import bubble_sort
from radix_sort import radix_sort


def main():
    for algorithm, sizes in [
        (bogo_sort, [5, 10, 20]),
        (bubble_sort, [100, 1000, 10000]),
        (radix_sort, [100, 1000, 10000, 100000, 1000000]),
    ]:
        for size in sizes:
            test_func = setup_test(algorithm, size)
            results = run_test(test_func)
            report_results(algorithm, size, results)


def setup_test(algorithm, size):
    test_data = numpy.random.randint(0, 1000, size)

    def func():
        return algorithm(test_data.copy())

    return func


def run_test(func):
    results = []
    for _ in range(3):

        try:
            with cProfile.Profile() as profile:

                @func_set_timeout(10)
                def do_test():
                    return profile.runcall(func)

                do_test()

                profile.print_stats()
                s = io.StringIO()
                ps = pstats.Stats(profile, stream=s)
                ps.print_stats()

            result = s.getvalue().split("\n")[0].strip()
        except FunctionTimedOut:
            result = "Test timed out."
            pass

        results.append(result)
    return results


def report_results(algorithm: Callable, size, results):
    print(algorithm.__name__, size, results)


if __name__ == "__main__":
    main()
