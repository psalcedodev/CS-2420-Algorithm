import random
import sys
from randomlist import createRandomList
from bubble import bubbleSort
from shaker import shakerSort
from selection import selectionSort


def main():

    # # *Bubble sort
    # a = createRandomList(10)
    # # Slice the array
    # print(a)
    # b = bubbleSort(a)
    # # b = shakerSort(a)
    # # b = selectionSort(a)
    # print(b)

    # # *Bubble sort
    # a = createRandomList(10)
    # # Slice the array
    # print(a)

    # b = shakerSort(a)

    # print(b)

    # *Bubble sort
    a = ["P", "S", "A", "W", "J", "T", "H", "Y"]
    # Slice the array
    print(a)

    b = quicksort(a)
    print(b)

    if a != b:
        print("Nope, try again")


if __name__ == "__main__":
    main()
