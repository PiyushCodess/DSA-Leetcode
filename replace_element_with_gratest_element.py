def replaceElements(arr):
    n = len(arr)
    max_so_far = -1
    for i in range(n - 1, -1, -1):
        new_val = max_so_far
        max_so_far = max(max_so_far, arr[i])
        arr[i] = new_val
    return arr


print(replaceElements([400]))  