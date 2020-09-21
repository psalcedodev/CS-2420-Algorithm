def shakerSort(a):
    done = False
    while done == False:
        done = True
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                done = False
                a[i], a[i + 1] = a[i+1], a[i]
        if done == True:
            break
        done = True

        for i in range(len(a) - 2, -1, -1):
            if a[i] > a[i + 1]:
                done = False
                a[i], a[i + 1] = a[i+1], a[i]
        if done == True:
            break
    return a
