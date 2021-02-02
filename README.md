# PIO_Lab1

A comparison of different sorting algorithms

## Results

# SENG3090 Lab 1 – Algorithms (and Python) | Kai Prince

### Your Tasks

Go to [https://github.com/TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) where you can find a multitude of common algorithms implemented in Python. Within each file you will find a function implementing that algorithm and an example main function that calls it.

For the following algorithms, profile the combinations indicated in the tables below. Report both the number of function calls and the time taken. Select random integers from the range 1 to 1000.

#### Sort: Bogo Sort

(Please ensure that all three trials at each size use the same array of random numbers)

| Input                      | Trial 1          | Trial 2      | Trial 3       |
| -------------------------- | ---------------- | ------------ | ------------- |
| Array of 5 random ints     | 9050 / 0.003     | 2355 / 0.002 | 11458 / 0.005 |
| Array of 10 random ints    | 21830283 / 8.502 | TIMEOUT      | TIMEOUT       |
| Array of 20 random ints \* | TIMEOUT          | TIMEOUT      | TIMEOUT       |

\* This could be bad

Question – what are the best and worst-case complexities (run times) of Bogo Sort? Why? See if you can come up with a reasonable answer before looking it up to confirm.

The best case for Bogo Sort is when the array is passed in fully sorted (verifying this still takes O(n)). The second best case is when the array is sorted in a single step, which is O(1), in addition to the verification time. The expected worst case is when every other possible combination has been tried, which is O((n+1)!). In practical terms however, since there can be duplicated guesses, the runtime is unbounded.

#### Sort: Bubble Sort

(Please ensure that all three trials at each size use the same array of random numbers)

| Input                         | Trial 1   | Trial 2   | Trial 3   |
| ----------------------------- | --------- | --------- | --------- |
| Array of 100 random ints      | 5 / 0.004 | 5 / 0.005 | 5 / 0.006 |
| Array of 1000 random ints     | 5 / 0.586 | 5 / 0.670 | 5 / 0.670 |
| Array of 10000 random ints \* | TIMEOUT   | TIMEOUT   | TIMEOUT   |

\* This is less bad, but still probably bad

Question – what is the worst-case complexity for Bubble Sort? (Feel free to look it up)

The worst-case complexity is O(n^2).

#### Sort: Radix Sort

(Please ensure that all three trials at each size use the same array of random numbers)

| Input                          | Trial 1         | Trial 2         | Trial 3         |
| ------------------------------ | --------------- | --------------- | --------------- |
| Array of 100 random ints       | 308 / 0.000     | 308 / 0.001     | 308 / 0.000     |
| Array of 1000 random ints      | 3008 / 0.007    | 3008 / 0.005    | 3008 / 0.005    |
| Array of 10000 random ints     | 30008 / 0.060   | 30008 / 0.050   | 30008 / 0.055   |
| Array of 100000 random ints \* | 300008 / 0.444  | 300008 / 0.421  | 300008 / 0.406  |
| Array of 1M random ints \*\*   | 3000008 / 3.566 | 3000008 / 3.743 | 3000008 / 4.273 |

\* This is no longer bad

\*\* This may be bad, but not necessarily because of the algorithm

Question – do you see a pattern in the reported profile data? Can you infer / guess the runtime of radix sort? See if you can tell from your data, before looking it up. What is the downside / compromise of using radix sort?

The runtime of radix sort is O(n). The compromise is the increased memory requirements. Radix sort uses buckets, which means the whole array must be held in memory to be sorted.

#### Search: Binary Search

Please use the Binary Search algorithm from the GitHub site, not the one from the slides. Use the function binary_search(), not any of the variants.

Please note that Binary Search requires that the is already sorted – use any sort you wish, but please don&#39;t include it in the timing information you collect.

(Please ensure that all three trials at each size use the same array of random numbers and search target)

| Input                          | Trial 1   | Trial 2   | Trial 3   |
| ------------------------------ | --------- | --------- | --------- |
| Array of 100 random ints       | 5 / 0.000 | 5 / 0.000 | 5 / 0.000 |
| Array of 1000 random ints      | 5 / 0.000 | 5 / 0.000 | 5 / 0.000 |
| Array of 10000 random ints     | 5 / 0.000 | 5 / 0.000 | 5 / 0.000 |
| Array of 100000 random ints \* | 5 / 0.000 | 5 / 0.000 | 5 / 0.000 |
| Array of 1M random ints \*\*   | 5 / 0.000 | 5 / 0.000 | 5 / 0.000 |

\* This is no longer bad

\*\* This may be bad due to the sort, but not the search

Question: What is the running time of binary search? Why is it &quot;good&quot;?

The running time is O(logn), which mean the runtime grows very slowly in proportion to the number of elements. It is a very fast sorting algorithm that can handle large amounts of data.
