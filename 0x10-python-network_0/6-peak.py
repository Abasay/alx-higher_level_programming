#!/usr/bin/python3
#python script to find the peak number in a list of integers

def find_peak(list_of_integers):
    """
    A function to find the peak in a list of integers
     Args:
          list_of_integers (int) : list of integers to check
    """
    sort_array = sorted(list_of_integers)
    if len(list_of_integers) == 0:
        return None

    return sort_array[-1]
