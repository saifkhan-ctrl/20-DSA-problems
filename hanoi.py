def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 0:
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print(f"Move disk {n} from {source} to {destination}")

    tower_of_hanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter number of disks: "))

if n < 0:
    print("Enter a non-negative number")
else:
    tower_of_hanoi(n, "A", "B", "C")