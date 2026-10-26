def count_occurrences(arr, target):
    first = -1
    last = -1
    low, high = 0, len(arr) - 1

    # Find first occurrence
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            first = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if first == -1:
        return 0

    low, high = first, len(arr) - 1

    # Find last occurrence
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            last = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return last - first + 1


arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

print("Count:", count_occurrences(arr, target))