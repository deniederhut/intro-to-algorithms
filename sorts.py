#!/bin/env python

def insertion_sort(array):
    item_ix = 1
    while item_ix < len(array):
        item_value = array[item_ix]
        search_ix = item_ix - 1
        while (search_ix >= 0) and (item_value < array[search_ix]):
            array[search_ix + 1] = array[search_ix]
            search_ix -= 1
        array[search_ix + 1] = item_value
        item_ix += 1
    return array
