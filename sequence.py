def print_subsequences(s, index=0, current=""):
    if index == len(s):
        print(repr(current))
        return

    # Exclude the current character
    print_subsequences(s, index + 1, current)

    # Include the current character
    print_subsequences(s, index + 1, current + s[index])


s = input("Enter a string: ")
print_subsequences(s)