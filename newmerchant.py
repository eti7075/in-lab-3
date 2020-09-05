import sys
from dataclasses import dataclass


@dataclass
class merchant:
    merch_name: str
    loc: str


def read_merchant(filename: str) -> [merchant]:
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
    if len(data) == 0:
        return []
    else:
        pivot = int(data[0].loc)
        less, equal, greater = partition(data, pivot)
        return quick_sort(less) + equal + quick_sort(greater)

def main(filename: str):
    Mlst = read_merchant(filename)
    sorted_merchants = quick_sort(Mlst)
    for merchant in sorted_merchants:
        print(merchant.merch_name + " " + merchant.loc)
    print(sorted_merchants[len(Mlst)//2].merch_name + " " + sorted_merchants[len(Mlst)//2].loc)


if __name__ == '__main__':
    fn = sys.argv
    main(fn[1])

