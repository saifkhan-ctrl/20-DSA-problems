def next_greater_element(arr):
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr)):
        # Resolve elements smaller than the current element
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            result[index] = arr[i]

        stack.append(i)

    return result


arr = list(map(int, input("Enter array elements: ").split()))
print("Next greater elements:", next_greater_element(arr))