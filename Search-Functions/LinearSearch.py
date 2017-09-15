def linear_search(arr, key, start=0):
    for i in range(start, len(arr)):
        if arr[i] == key:
            return i
    return -1
