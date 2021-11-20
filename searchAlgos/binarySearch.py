# look for x in arr, return the index of x in arr if found, else return -1.
def binaySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r-1) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binaySearch(arr, l, mid-1, x)
        else:
            return binaySearch(arr, mid, r, x)
    else:
        return -1
