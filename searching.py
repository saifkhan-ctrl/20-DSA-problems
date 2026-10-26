def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            high = mid - 1  # Search left side
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


def last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            low = mid + 1  # Search right side
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

print("First occurrence:", first_occurrence(arr, target))
print("Last occurrence:", last_occurrence(arr, target))