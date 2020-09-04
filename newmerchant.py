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


def partition(data: list[str], pivot: int) -> Tuple(list[str], list[str], list[str]):
    less, equal, greater = [], [], []
    for element in data:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            greater.append(element)
        else:
            equal.append(element)
    return less, equal, greater


def main(filename: str):
    Mlst = read_merchant(filename)
    for merchant in Mlst:
        print(merchant.merch_name + " " + merchant.loc)


if __name__ == '__main__':
    fn = sys.argv
    main(fn[1])

