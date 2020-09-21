def selectionSort(a):
    # * Checks the rang of the lenght of a at last position
    for i in range(len(a)):

        # * Declares the variable smallest
        smallest = i

        # * Checks
        for j in range(smallest + 1, len(a)):
            if a[j] < a[smallest]:
                smallest = j
        a[i], a[smallest] = a[smallest], a[i]
    return a
