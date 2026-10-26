def print_numbers(n):
    if n == 0:  # Base case
        return

    print_numbers(n - 1)
    print(n)


n = int(input("Enter N: "))
print_numbers(n)