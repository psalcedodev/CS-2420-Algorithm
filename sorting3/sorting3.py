import sys
import math
import random


class Counter:

    def __init__(self):
        self.mCompares = 0
        self.mSwaps = 0


def create_random_list(n):
    a = []
    for i in range(n):
        r = random.randrange(0, n)
        a.append(r)
    return a


def create_random_mostly_sorted(n):
    a = []
    for i in range(n):
        r = random.randrange(0, n)
        a.append(r)
    a.sort()
    a[0], a[len(a) - 1], = a[len(a) - 1], a[0]
    return a


def real_quick_sort(a, count):
    quick_sort(a, 0, len(a) - 1, False, count)


def modified_quick_sort(a, count):
    quick_sort(a, 0, len(a) - 1, True, count)


def quick_sort(a, low, high, mod, count):
    # basecase
    if high - low <= 0:
        return
    # do 1 pass of quicksort
    if mod:
        mid = int((high + low) / 2)
        a[low], a[mid] = a[mid], a[low]
        count.mSwaps += 1
    lmgt = low + 1
    for i in range(low + 1, high + 1):
        count.mCompares += 1
        if a[i] < a[low]:
            a[i], a[lmgt] = a[lmgt], a[i]
            count.mSwaps += 1  # Probably missing?
            lmgt += 1

    pivotindex = lmgt - 1
    a[low], a[pivotindex] = a[pivotindex], a[low]
    count.mSwaps += 1  # Probably missing?

    # lefthalf
    quick_sort(a, low, pivotindex - 1, mod, count)
    # righthalf

    quick_sort(a, pivotindex + 1, high, mod, count)


def merge_sort(a, count):
    # basecase
    if len(a) <= 1:
        return
    # split
    l = a[0: int(len(a)/2)]
    r = a[int(len(a)/2): int(len(a))]
    count.mSwaps += len(a)
    # recurse
    merge_sort(l, count)
    merge_sort(r, count)

    # merge l and r back onto a
    i = 0
    j = 0
    k = 0
    while (len(l) - 1) >= i and (len(r) - 1) >= j:
        count.mCompares += 1
        if l[i] <= r[j]:
            count.mSwaps += 1  # Probably missing?
            a[k] = l[i]
            i += 1
            k += 1
        else:
            count.mSwaps += 1  # Probably missing?
            a[k] = r[j]
            j += 1
            k += 1
    while (len(l) - 1) >= i:
        count.mSwaps += 1  # Probably missing?
        a[k] = l[i]
        i += 1
        k += 1
    while (len(r) - 1) >= j:
        count.mSwaps += 1  # Probably missing?
        a[k] = r[j]
        j += 1
        k += 1


def hash_sort(a, count):
    frequency = []
    for i in range(len(a)):
        frequency.append(0)
    for i in range(len(a)):
        frequency[a[i]] += 1
    counter = 0
    for i in range(len(frequency)):
        for j in range(frequency[i]):
            count.mSwaps += 1  # Probably missing?
            a[counter] = i
            counter += 1


def bubble_sort(a, count):
    done = False
    while done == False:
        done = True
        for i in range(len(a) - 1):
            count.mCompares += 1
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i+1], a[i]
                count.mSwaps += 1
                done = False
    return a


def shaker_sort(a, count):
    done = False
    while done == False:
        done = True
        # Pass from left to right
        for i in range(len(a) - 1):
            count.mCompares += 1
            if a[i] > a[i + 1]:
                done = False
                a[i], a[i + 1] = a[i+1], a[i]
                count.mSwaps += 1
        if done == True:
            break
        # pass from right to left
        for i in range(len(a) - 2, -1, -1):
            count.mCompares += 1
            if a[i] > a[i + 1]:
                done = False
                a[i], a[i + 1] = a[i+1], a[i]
                count.mSwaps += 1
        if done == True:
            break
    return a


def selection_sort(a, count):
    for i in range(len(a) - 1):
        smallest = i
        for j in range(smallest + 1, len(a)):
            count.mCompares += 1
            if a[j] < a[smallest]:
                smallest = j
        if smallest != i:
            a[i], a[smallest] = a[smallest], a[i]
            count.mSwaps += 1
    return a


def main():
    sys.setrecursionlimit(5000)
    sort_alg = [bubble_sort, shaker_sort, selection_sort,
                merge_sort, real_quick_sort, modified_quick_sort, hash_sort]
    print("      Bubble     Shaker Selection Quick   Mquick  Merge\t  Hash")
    for i in range(3, 13):
        size = 2 ** i
        print("%4i" % (i), end="\t")
        for sort in sort_alg:
            a = create_random_list(size)
            # a = create_random_mostly_sorted(size)
            count = Counter()
            sort(a[:], count)
            if sort.__name__ != "hash_sort":
                swaps = round(math.log(count.mSwaps), 2)
            else:
                swaps = i
            format(swaps, "6.2f")
            print(swaps, end="\t")
        print()

    # sys.setrecursionlimit(5000)
    # sort_algorithmns = [bubble_sort, shaker_sort, selection_sort, merge_sort, real_quick_sort, modified_quick_sort, hash_sort]
    # print("      Bubble     Shaker Selection Quick   Mquick  Merge\t  Hash")
    # for i in range(3, 13):
    #     size = 2 ** i
    #     print("%4i" % (i), end="\t")
    #     for sort in sort_algorithmns:
    #         a = create_random_mostly_sorted(size)
    #         count = Counter()
    #         sort(a[:], count)
    #         if sort.__name__ != "hash_sort":
    #             swaps = round(math.log(count.mSwaps), 2)
    #         else:
    #             swaps = i
    #         # formatstring = "%6.2f"
    #         # print(formatstring % (swaps), end="\t")
    #         format(swaps, "6.2f")
    #         print(swaps, end="\t  ")
    #     print()


if __name__ == "__main__":
    main()
