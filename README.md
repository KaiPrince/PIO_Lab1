# SENG3090 Lab 1 – Algorithms (and Python) | Kai Prince

A comparison of different sorting algorithms

## Results

<< number of calls / duration in seconds >>

#### Sort: Bogo Sort

| Input                   | Trial 1          | Trial 2      | Trial 3       |
| ----------------------- | ---------------- | ------------ | ------------- |
| Array of 5 random ints  | 9050 / 0.003     | 2355 / 0.002 | 11458 / 0.005 |
| Array of 10 random ints | 21830283 / 8.502 | TIMEOUT      | TIMEOUT       |
| Array of 20 random ints | TIMEOUT          | TIMEOUT      | TIMEOUT       |

#### Sort: Bubble Sort

| Input                      | Trial 1   | Trial 2   | Trial 3   |
| -------------------------- | --------- | --------- | --------- |
| Array of 100 random ints   | 5 / 0.004 | 5 / 0.005 | 5 / 0.006 |
| Array of 1000 random ints  | 5 / 0.586 | 5 / 0.670 | 5 / 0.670 |
| Array of 10000 random ints | TIMEOUT   | TIMEOUT   | TIMEOUT   |

#### Sort: Radix Sort

| Input                       | Trial 1         | Trial 2         | Trial 3         |
| --------------------------- | --------------- | --------------- | --------------- |
| Array of 100 random ints    | 308 / 0.000     | 308 / 0.001     | 308 / 0.000     |
| Array of 1000 random ints   | 3008 / 0.007    | 3008 / 0.005    | 3008 / 0.005    |
| Array of 10000 random ints  | 30008 / 0.060   | 30008 / 0.050   | 30008 / 0.055   |
| Array of 100000 random ints | 300008 / 0.444  | 300008 / 0.421  | 300008 / 0.406  |
| Array of 1M random ints     | 3000008 / 3.566 | 3000008 / 3.743 | 3000008 / 4.273 |

#### Search: Binary Search

| Input                       | Trial 1   | Trial 2   | Trial 3   |
| --------------------------- | --------- | --------- | --------- |
| Array of 100 random ints    | 5 / 0.000 | 5 / 0.000 | 5 / 0.000 |
| Array of 1000 random ints   | 5 / 0.000 | 5 / 0.000 | 5 / 0.000 |
| Array of 10000 random ints  | 5 / 0.000 | 5 / 0.000 | 5 / 0.000 |
| Array of 100000 random ints | 5 / 0.000 | 5 / 0.000 | 5 / 0.000 |
| Array of 1M random ints     | 5 / 0.000 | 5 / 0.000 | 5 / 0.000 |
