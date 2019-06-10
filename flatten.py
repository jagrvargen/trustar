#!/usr/bin/env python3
"""
   Contains a simple function which will flatten an array
   of arbitrarily nested integers. 
"""

def flatten(arr, flat_arr=None):
    """ Flattens an array of nested integers. """
    if type(arr) is not list:
        raise TypeError

    flat_arr = [] if flat_arr is None else flat_arr

    for item in arr:
        if type(item) is int:
            flat_arr.append(item)
        else:
            flatten(item, flat_arr)

    return flat_arr
