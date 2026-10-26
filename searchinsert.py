def search_insert_position(arr, target):
    low, high = 0, len(arr)

    while low < high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low


arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

print("Insert position:", search_insert_position(arr, target))