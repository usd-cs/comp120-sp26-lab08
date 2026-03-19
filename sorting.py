"""
Module: sorting

Implementation of some (non-recursive) sorting algorithms.
"""

def selection_sort(arr: list[int]) -> None:
    """
    Uses selection sort to sort the given list of integers (arr).
    """
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap only if a smaller element was found
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr: list[int]) -> None:
    """
    Uses insertion sort to sort the given list of integers (arr).
    """

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key in its correct location
        arr[j + 1] = key
