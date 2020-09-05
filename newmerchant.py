"""
Author: Ethan Iannicelli
project: In-Lab-3
merchant reading and sorting
"""

import sys
from dataclasses import dataclass

@dataclass
class merchant:
    """
    merchant class
    merch_name --> name of the merchant
    loc --> location of the merchant
    """
    merch_name: str
    loc: str

def read_merchant(filename: str) -> [merchant]:
    """
    reads from the given file and creates and returns a list of merchants
    :param filename: name of the file to read from
    :return: list of merchants read from file
    """
    merches = []
    with open(filename) as f:
        for line in f:
            fields = line.split(' ')
            merches.append(merchant(
                merch_name=fields[0],
                loc=fields[1]
            ))
    return merches

def partition(data: [merchant], pivot: int) -> ([merchant], [merchant], [merchant]):
    """
    finds the partitioned lists of the given list, part of quicksort function
    :param data: list of merchants passed in
    :param pivot: pivot for quicksort
    :return: lists in reltaion of the pivot
    """
    less, equal, greater = [], [], []
    for element in data:
        if int(element.loc) < pivot:
            less.append(element)
        elif int(element.loc) > pivot:
            greater.append(element)
        else:
            equal.append(element)
    return less, equal, greater

def quick_sort(data: [merchant]) -> [merchant]:
    """
    the recursive function of the quicksort, finds the sorted list
    :param data: given list of merchants (unsorted)
    :return: sorted list of merchants
    """
    if len(data) == 0:
        return []
    else:
        pivot = int(data[0].loc)
        less, equal, greater = partition(data, pivot)
        return quick_sort(less) + equal + quick_sort(greater)

def main(filename: str):
    """
    main function, reads file to a list, sorts list, prints sorted list and optimal (median) position for the new store
    """
    Mlst = read_merchant(filename)
    sorted_merchants = quick_sort(Mlst)
    for merchant in sorted_merchants:
        print(merchant.merch_name + " " + merchant.loc)
    print(sorted_merchants[len(Mlst)//2].merch_name + " " + sorted_merchants[len(Mlst)//2].loc)

if __name__ == '__main__':
    """
    runs main function with the inputted file from the cmd line
    """
    fn = sys.argv
    main(fn[1])

