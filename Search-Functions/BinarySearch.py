def binary_search(arr, key):
    min = 0
    max = len(arr) - 1
    while True:
        if max < min:
            return -1
        m = (min + max) // 2
        if arr[m] < key:
            min = m + 1
        elif arr[m] > key:
            max = m - 1
        else:
            return m
