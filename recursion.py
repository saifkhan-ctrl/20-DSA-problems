def is_sorted(arr, index=0):
    if index >= len(arr) - 1:
        return True

    if arr[index] > arr[index + 1]:
        return False

    return is_sorted(arr, index + 1)


arr = list(map(int, input("Enter array elements: ").split()))

if is_sorted(arr):
    print("Array is sorted")
else:
    print("Array is not sorted")