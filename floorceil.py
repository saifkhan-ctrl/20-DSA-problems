def find_floor_ceil(arr, target):
    low, high = 0, len(arr) - 1
    floor_value = None
    ceil_value = None

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return arr[mid], arr[mid]

        elif arr[mid] < target:
            floor_value = arr[mid]
            low = mid + 1

        else:
            ceil_value = arr[mid]
            high = mid - 1

    return floor_value, ceil_value


arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

floor_value, ceil_value = find_floor_ceil(arr, target)

print("Floor:", floor_value)
print("Ceil:", ceil_value)