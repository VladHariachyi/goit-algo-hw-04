from enum import Enum
from random import random
from sorting_fns import (
    bubble_sort,
    insertion_sort,
    selection_sort,
    quicksort,
    merge_sort,
    shell_sort,
    radix_sort
)

def generate_random_data(size = 100) -> list[float]:
    return [int(random() * 1000) for _ in range(size)]


class DataTypes(Enum):
    SMALL_DATA = "Small data"
    BIG_DATA = "Big data"
    REVERSED_DATA = "Reversed data"
    SORTED_FOR_HALF_DATA = "Sorted for half data"
    RANDOM_DATA = "Random data"

    def __str__(self):
        return self.value


class SortingFunctions(Enum):
    BUBBLE_SORT = "Bubble sort"
    INSERTION_SORT = "Insertion sort"
    SELECTION_SORT = "Selection sort"
    QUICK_SORT = "Quick sort"
    MERGE_SORT = "Merge sort"
    SHELL_SORT =  "Shell sort"
    RADIX_SORT = "Radix sort"
    TIM_SORT = "Tim sort"

    def __str__(self):
        return self.value

DATA = {
    DataTypes.SMALL_DATA: list(range(100)),
    DataTypes.BIG_DATA: list(range(10_000)),
    DataTypes.REVERSED_DATA: list(reversed(range(10_000))),
    DataTypes.SORTED_FOR_HALF_DATA: (
        list(sorted(generate_random_data(5_000))) + 
        list(generate_random_data(5_000))
    ),
    DataTypes.RANDOM_DATA: generate_random_data(10_000)
}


SORTING_FUNCTIONS = {
    SortingFunctions.BUBBLE_SORT: bubble_sort,
    SortingFunctions.INSERTION_SORT: insertion_sort,
    SortingFunctions.SELECTION_SORT: selection_sort,
    SortingFunctions.QUICK_SORT: quicksort,
    SortingFunctions.MERGE_SORT: merge_sort,
    SortingFunctions.SHELL_SORT: shell_sort,
    SortingFunctions.RADIX_SORT: radix_sort,
    SortingFunctions.TIM_SORT: sorted
}


CASES = [
    # Bubble Sort
    {
        "scenario": f"{SortingFunctions.BUBBLE_SORT} with {DataTypes.SMALL_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.BUBBLE_SORT],
        "data": DATA[DataTypes.SMALL_DATA],
    },
    {
        "scenario": f"{SortingFunctions.BUBBLE_SORT} with {DataTypes.BIG_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.BUBBLE_SORT],
        "data": DATA[DataTypes.BIG_DATA],
    },
    {
        "scenario": f"{SortingFunctions.BUBBLE_SORT} with {DataTypes.REVERSED_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.BUBBLE_SORT],
        "data": DATA[DataTypes.REVERSED_DATA],
    },
    {
        "scenario": f"{SortingFunctions.BUBBLE_SORT} with {DataTypes.SORTED_FOR_HALF_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.BUBBLE_SORT],
        "data": DATA[DataTypes.SORTED_FOR_HALF_DATA],
    },
    {
        "scenario": f"{SortingFunctions.BUBBLE_SORT} with {DataTypes.RANDOM_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.BUBBLE_SORT],
        "data": DATA[DataTypes.RANDOM_DATA],
    },
    # Insertion Sort
    {
        "scenario": f"{SortingFunctions.INSERTION_SORT} with {DataTypes.SMALL_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.INSERTION_SORT],
        "data": DATA[DataTypes.SMALL_DATA],
    },
    {
        "scenario": f"{SortingFunctions.INSERTION_SORT} with {DataTypes.BIG_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.INSERTION_SORT],
        "data": DATA[DataTypes.BIG_DATA],
    },
    {
        "scenario": f"{SortingFunctions.INSERTION_SORT} with {DataTypes.REVERSED_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.INSERTION_SORT],
        "data": DATA[DataTypes.REVERSED_DATA],
    },
    {
        "scenario": f"{SortingFunctions.INSERTION_SORT} with {DataTypes.SORTED_FOR_HALF_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.INSERTION_SORT],
        "data": DATA[DataTypes.SORTED_FOR_HALF_DATA],
    },
    {
        "scenario": f"{SortingFunctions.INSERTION_SORT} with {DataTypes.RANDOM_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.INSERTION_SORT],
        "data": DATA[DataTypes.RANDOM_DATA],
    },
    # Selection Sort
    {
        "scenario": f"{SortingFunctions.SELECTION_SORT} with {DataTypes.SMALL_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.SELECTION_SORT],
        "data": DATA[DataTypes.SMALL_DATA],
    },
    {
        "scenario": f"{SortingFunctions.SELECTION_SORT} with {DataTypes.BIG_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.SELECTION_SORT],
        "data": DATA[DataTypes.BIG_DATA],
    },
    {
        "scenario": f"{SortingFunctions.SELECTION_SORT} with {DataTypes.REVERSED_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.SELECTION_SORT],
        "data": DATA[DataTypes.REVERSED_DATA],
    },
    {
        "scenario": f"{SortingFunctions.SELECTION_SORT} with {DataTypes.SORTED_FOR_HALF_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.SELECTION_SORT],
        "data": DATA[DataTypes.SORTED_FOR_HALF_DATA],
    },
    {
        "scenario": f"{SortingFunctions.SELECTION_SORT} with {DataTypes.RANDOM_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.SELECTION_SORT],
        "data": DATA[DataTypes.RANDOM_DATA],
    },
    # Quick Sort
    {
        "scenario": f"{SortingFunctions.QUICK_SORT} with {DataTypes.SMALL_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.QUICK_SORT],
        "data": DATA[DataTypes.SMALL_DATA],
    },
    {
        "scenario": f"{SortingFunctions.QUICK_SORT} with {DataTypes.BIG_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.QUICK_SORT],
        "data": DATA[DataTypes.BIG_DATA],
    },
    {
        "scenario": f"{SortingFunctions.QUICK_SORT} with {DataTypes.REVERSED_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.QUICK_SORT],
        "data": DATA[DataTypes.REVERSED_DATA],
    },
    {
        "scenario": f"{SortingFunctions.QUICK_SORT} with {DataTypes.SORTED_FOR_HALF_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.QUICK_SORT],
        "data": DATA[DataTypes.SORTED_FOR_HALF_DATA],
    },
    {
        "scenario": f"{SortingFunctions.QUICK_SORT} with {DataTypes.RANDOM_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.QUICK_SORT],
        "data": DATA[DataTypes.RANDOM_DATA],
    },
    # Merge Sort
    {
        "scenario": f"{SortingFunctions.MERGE_SORT} with {DataTypes.SMALL_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.MERGE_SORT],
        "data": DATA[DataTypes.SMALL_DATA],
    },
    {
        "scenario": f"{SortingFunctions.MERGE_SORT} with {DataTypes.BIG_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.MERGE_SORT],
        "data": DATA[DataTypes.BIG_DATA],
    },
    {
        "scenario": f"{SortingFunctions.MERGE_SORT} with {DataTypes.REVERSED_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.MERGE_SORT],
        "data": DATA[DataTypes.REVERSED_DATA],
    },
    {
        "scenario": f"{SortingFunctions.MERGE_SORT} with {DataTypes.SORTED_FOR_HALF_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.MERGE_SORT],
        "data": DATA[DataTypes.SORTED_FOR_HALF_DATA],
    },
    {
        "scenario": f"{SortingFunctions.MERGE_SORT} with {DataTypes.RANDOM_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.MERGE_SORT],
        "data": DATA[DataTypes.RANDOM_DATA],
    },
    # Shell Sort
    {
        "scenario": f"{SortingFunctions.SHELL_SORT} with {DataTypes.SMALL_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.SHELL_SORT],
        "data": DATA[DataTypes.SMALL_DATA],
    },
    {
        "scenario": f"{SortingFunctions.SHELL_SORT} with {DataTypes.BIG_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.SHELL_SORT],
        "data": DATA[DataTypes.BIG_DATA],
    },
    {
        "scenario": f"{SortingFunctions.SHELL_SORT} with {DataTypes.REVERSED_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.SHELL_SORT],
        "data":DATA[DataTypes.REVERSED_DATA],
    },
    {
        "scenario": f"{SortingFunctions.SHELL_SORT} with {DataTypes.SORTED_FOR_HALF_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.SHELL_SORT],
        "data": DATA[DataTypes.SORTED_FOR_HALF_DATA],
    },
    {
        "scenario": f"{SortingFunctions.SHELL_SORT} with {DataTypes.RANDOM_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.SHELL_SORT],
        "data": DATA[DataTypes.RANDOM_DATA],
    },
    # Radix Sort
    {
        "scenario": f"{SortingFunctions.RADIX_SORT} with {DataTypes.SMALL_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.RADIX_SORT],
        "data": DATA[DataTypes.SMALL_DATA],
    },
    {
        "scenario": f"{SortingFunctions.RADIX_SORT} with {DataTypes.BIG_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.RADIX_SORT],
        "data": DATA[DataTypes.BIG_DATA],
    },
    {
        "scenario": f"{SortingFunctions.RADIX_SORT} with {DataTypes.REVERSED_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.RADIX_SORT],
        "data":DATA[DataTypes.REVERSED_DATA],
    },
    {
        "scenario": f"{SortingFunctions.RADIX_SORT} with {DataTypes.SORTED_FOR_HALF_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.RADIX_SORT],
        "data": DATA[DataTypes.SORTED_FOR_HALF_DATA],
    },
    {
        "scenario": f"{SortingFunctions.RADIX_SORT} with {DataTypes.RANDOM_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.RADIX_SORT],
        "data": DATA[DataTypes.RANDOM_DATA],
    },
        # Tim Sort
    {
        "scenario": f"{SortingFunctions.TIM_SORT} with {DataTypes.SMALL_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.TIM_SORT],
        "data": DATA[DataTypes.SMALL_DATA],
    },
    {
        "scenario": f"{SortingFunctions.TIM_SORT} with {DataTypes.BIG_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.TIM_SORT],
        "data": DATA[DataTypes.BIG_DATA],
    },
    {
        "scenario": f"{SortingFunctions.TIM_SORT} with {DataTypes.REVERSED_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.TIM_SORT],
        "data":DATA[DataTypes.REVERSED_DATA],
    },
    {
        "scenario": f"{SortingFunctions.TIM_SORT} with {DataTypes.SORTED_FOR_HALF_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.TIM_SORT],
        "data": DATA[DataTypes.SORTED_FOR_HALF_DATA],
    },
    {
        "scenario": f"{SortingFunctions.TIM_SORT} with {DataTypes.RANDOM_DATA}",
        "sort_fn": SORTING_FUNCTIONS[SortingFunctions.TIM_SORT],
        "data": DATA[DataTypes.RANDOM_DATA],
    },
]