#!/usr/bin/python3
#python script to find the peak number in a list of integers

def find_peak(list_of_integers):
    """
    A function to find the peak in a list of integers
     Args:
          list_of_integers (int) : list of integers to check
    """
    peak = 0
    
    if len(list_of_integers) == 0:
        return None

    for i in range(0, len(list_of_integers)):
        if list_of_integers[i] > peak:
            peak = list_of_integers[i]
    return peak
