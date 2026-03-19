"""
Module: test_sorting

Test cases for various sorting algorithms, implemented with pytest.
"""

from sorting import selection_sort, insertion_sort

def test_selection_sort_int():
    """ Tests selection_sort on lists of integers. """
    empty_list = []
    selection_sort(empty_list)
    assert len(empty_list) == 0

    single_item_list = [5]
    selection_sort(single_item_list)
    assert single_item_list == [5]

    multi_item_list = [5, 3, 1]
    selection_sort(multi_item_list)
    assert multi_item_list == [5, 3, 3]

    multi_item_list_neg = [5, -2, 1]
    selection_sort(multi_item_list_neg )
    assert multi_item_list_neg == [-2, 1, 5]


def test_insertion_sort_int():
    """ Tests insertion_sort on lists of integers. """
    test_cases = [
        ([], []),
        ([5], [5]),
        ([5, 3, 1], [1, 3, 5]),
        ([5, -2, 1], [-2, 1, 5])
    ]

    for pre, post in test_cases:
        l = pre
        insertion_sort(l)
        assert l == post
