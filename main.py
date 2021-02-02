"""
 * Project Name: PIO_Lab1
 * File Name: main.py
 * Programmer: Kai Prince
 * Date: Tue, Feb 02, 2021
 * Description: This program compares sorting algorithms.
"""
import time
from typing import Callable
from bogo_sort import bogo_sort
from bubble_sort import bubble_sort
from radix_sort import radix_sort
from func_timeout import func_set_timeout
from func_timeout.exceptions import FunctionTimedOut
import numpy
import cProfile


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

    @func_set_timeout(10)
    def func():
        with cProfile.Profile() as profile:
            profile.runcall(algorithm, test_data.copy())

        profile.print_stats()

    return func


def run_test(func):
    results = []
    for _ in range(3):
        start = time.process_time()

        try:
            func()
        except FunctionTimedOut:
            print("Test timed out.")
            pass

        result = time.process_time() - start
        results.append(result)
    return results


def report_results(algorithm: Callable, size, results):
    print(algorithm.__name__, size, results)


if __name__ == "__main__":
    main()
