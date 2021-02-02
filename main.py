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

from binary_search import binary_search
from bogo_sort import bogo_sort
from bubble_sort import bubble_sort
from radix_sort import radix_sort


def main():
    # Sorting
    for algorithm, sizes in [
        (bogo_sort, [5, 10, 20]),
        (bubble_sort, [100, 1000, 10000]),
        (radix_sort, [100, 1000, 10000, 100000, 1000000]),
    ]:
        for size in sizes:
            test_data, run_func = setup_sort_test(algorithm, size)
            results = run_test(run_func, test_data)
            report_results(algorithm, size, results)

    # Searching
    for algorithm, sizes in [(binary_search, [100, 1000, 10000, 100000, 1000000])]:
        for size in sizes:
            sorted_test_data, run_func = setup_search_test(algorithm, size)
            results = run_test(run_func, sorted_test_data)
            report_results(algorithm, size, results)


def setup_sort_test(algorithm, size):
    test_data = get_test_data(size)

    def run_func(data):
        return algorithm(data)

    return (test_data, run_func)


def setup_search_test(algorithm, size):
    test_data = get_test_data(size)

    sorted_test_data = radix_sort(test_data)

    def run_func(data):
        return algorithm(data, test_data[0])

    return (sorted_test_data, run_func)


def get_test_data(size):
    test_data = numpy.random.randint(0, 1000, size)

    return test_data


def run_test(func, test_data):
    results = []

    for _ in range(3):
        test_data_copy = test_data.copy()

        @func_set_timeout(10)
        def do_test():
            with cProfile.Profile() as profile:
                profile.runcall(func, test_data_copy)
                # profile.print_stats()

                s = io.StringIO()
                ps = pstats.Stats(profile, stream=s)
                ps.print_stats()

            return s.getvalue()

        try:
            output = do_test()

            result = output.split("\n")[0].strip()
        except FunctionTimedOut:
            result = "Test timed out."
            pass

        results.append(result)
    return results


def report_results(algorithm: Callable, size, results):
    print(algorithm.__name__, size, results)


if __name__ == "__main__":
    main()
