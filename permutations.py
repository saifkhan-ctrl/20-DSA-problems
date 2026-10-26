def permutations(s, index=0):
    if index == len(s):
        print(s)
        return

    chars = list(s)

    for i in range(index, len(chars)):
        # Swap the current character into position
        chars[index], chars[i] = chars[i], chars[index]

        permutations("".join(chars), index + 1)


s = input("Enter a string: ")
permutations(s)