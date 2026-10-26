def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter N: "))

if n < 0:
    print("Enter a non-negative integer")
else:
    print("Fibonacci number:", fibonacci(n))