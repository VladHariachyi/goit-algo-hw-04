# Sorting algorithms performance comparison

## Metrics (time in sec)

| Algorithm | Small data | Big data | Reversed | Sorted for half | Random |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Bubble sort** | 0.0001 | 1.6657 | 3.5954 | 2.5623 | 2.8793 |
| **Insertion sort** | 0.0000 | 0.0006 | 2.3770 | 0.9056 | 1.2210 |
| **Selection sort** | 0.0001 | 1.1951 | 1.2658 | 1.2158 | 1.2250 |
| **Quick sort** | 0.0001 | 0.0061 | 0.0064 | 0.0144 | 0.0058 |
| **Merge sort** | 0.0001 | 0.0092 | 0.0093 | 0.0110 | 0.0124 |
| **Shell sort** | 0.0000 | 0.0058 | 0.0095 | 0.0131 | 0.0149 |
| **Radix sort** | 0.0000 | 0.0079 | 0.0080 | 0.0063 | 0.0072 |
| **Timsort (otb)** | **0.0000** | **0.0000** | **0.0001** | **0.0005** | **0.0008** |

---

## Conclusion

* **Absolute Leader (Timsort):** Instant execution (~0.001s) across all datasets due to built-in Python C-level optimizations.
* **Efficient Group:** **Quick, Shell, Merge, and Radix** sorts perform exceptionally fast (~0.015s) on all large datasets.
* **Inefficient Group:** 
  * **Bubble sort** is the worst performer, peaking at 3.59s on reversed data.
  * **Selection sort** is consistently slow (~1.2s) regardless of initial data order.
  * **Insertion sort** struggles on random/reversed data, but shines on nearly sorted arrays (0.0006s).