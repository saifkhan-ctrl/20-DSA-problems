def power(x, n):
    if n == 0:
        return 1

    if n < 0:
        return 1 / power(x, -n)

    half = power(x, n // 2)

    if n % 2 == 0:
        return half * half

    return x * half * half


x = float(input("Enter base x: "))
n = int(input("Enter exponent n: "))

if x == 0 and n < 0:
    print("Undefined: zero cannot have a negative exponent")
else:
    print("Result:", power(x, n))