def subset_sum(arr, target, index=0):
    if target == 0:
        return True

    if index == len(arr):
        return False

    # Try including the current element
    if subset_sum(arr, target - arr[index], index + 1):
        return True

    # Try excluding the current element
    return subset_sum(arr, target, index + 1)


arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target sum S: "))

if subset_sum(arr, target):
    print("Subset with the given sum exists")
else:
    print("Subset with the given sum does not exist")