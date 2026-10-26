def merge_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    merged = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Add remaining elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])

    return merged


arr1 = list(map(int, input("Enter first sorted array: ").split()))
arr2 = list(map(int, input("Enter second sorted array: ").split()))

print("Merged array:", merge_sorted_arrays(arr1, arr2))