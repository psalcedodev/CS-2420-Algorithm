import random
import sys

# Creates a random list for us to use throught our sortings


def createRandomList(n):
    # Initialize our empty list
    a = []
    # Initiates a foor loop and goes n times. We set the value of "n" below by calling createRandomList()
    # For example createRandomList(10). It means that the for loop will run 10 times
    for i in range(n):
        # The numbers are random from 0 to n. As specified, n is the value we set above. So our random.rangrange will grab a random number from 0 to 10.
        r = random.randrange(0, n)
        # After we get the random number, we just need to append it to our list and finally return it.
        a.append(r)
    return a


def quick_sort(a):
    # Quick sort grabs the value of "a" which is passed to quick_sort in main()
    quicksort(a, 0, len(a) - 1, False)


def modified_quick_sort(a):
    # Quick sort grabs the value of "a" which is passed to modified_quick_sort in main()
    quicksort(a, 0, len(a) - 1, True)


def quicksort(a, low, high, mod):
    # basecase
    if high - low <= 0:
        return
    # do 1 pass of quicksort
    if mod:
        mid = int((high + low) / 2)
        a[low], a[mid] = a[mid], a[low]
    lmgt = low + 1
    for i in range(low + 1, high + 1):
        if a[i] < a[low]:
            a[i], a[lmgt] = a[lmgt], a[i]
            lmgt += 1

    pivotindex = lmgt - 1
    a[low], a[pivotindex] = a[pivotindex], a[low]

    # recurse
    # lefthalf
    quicksort(a, low, pivotindex - 1, mod)
    # righthalf
    quicksort(a, pivotindex + 1, high, mod)


def mergesort(a):
    # basecase
    if len(a) <= 1:
        return
    # split
    l = a[0: int(len(a)/2)]
    r = a[int(len(a)/2): int(len(a))]
    # recurse
    mergesort(l)
    mergesort(r)

    # merge l and r back onto a
    i = 0
    j = 0
    k = 0
    # print(a)
    while (len(l) - 1) >= i and (len(r) - 1) >= j:
        if l[i] <= r[j]:
            a[k] = l[i]
            i += 1
            k += 1
        else:
            a[k] = r[j]
            j += 1
            k += 1
    while (len(l) - 1) >= i:
        a[k] = l[i]
        i += 1
        k += 1
    while (len(r) - 1) >= j:
        a[k] = r[j]
        j += 1
        k += 1
    # print(a)


# def counting(a):

#     frequency = []
#     for i in range(len(a)):
#         frequency.append(0)
#     for i in range(len(a)):
#         frequency[a[i]] += 1
#     count = 0
#     for i in range(len(frequency)):
#         for j in range(frequency[i]):
#             a[count] = i
#             count += 1


def main():
    count = 0
    for sort in (quick_sort, modified_quick_sort, mergesort):

        test_array = [4, 7, 2, 1, 8, 3, 9, 5]
        a = ["P", "S", "A", "W", "J", "T", "H", "Y"]
        b = a[:]
        print('[Random Numbers]')
        print(a)
        print()
        if(count == 0):
            print('[Quick Sort]')
        elif(count == 1):
            print('[Modified Quick Sort]')
        elif(count == 2):
            print('[Merge Sort]')
        elif(count == 3):
            print('[Counting Sort]')
        sort(a)
        b.sort()
        print(b)
        print('==================================================')
        print()
        count += 1

    if a != b:
        print("Too bad, try again")


main()
