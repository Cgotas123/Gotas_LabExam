def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)


try:
    n = int(input("Input values: "))

    if n <= 0:
        print("Error: Please enter a positive integer for dis ks.")
    else:
        print(f"\nSolution for Tower of Hanoi with {n} disks:\n")
        tower_of_hanoi(n, "4", "2", "3")
                 
except ValueError:
    print("Error: Please enter a valid integer.")



    