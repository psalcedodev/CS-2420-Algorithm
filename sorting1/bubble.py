def bubbleSort(a):
    done = True
    while done == True:
        done = False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i+1], a[i]
                done = True

         
    return a
