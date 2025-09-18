def gcd(x, y):

    if y == 0:
        return x
    return gcd(y, x % y)

def lcm(x, y):

    return abs(x * y) // gcd(x, y)
try:
    x = int(input("Enter a value for x: "))
    y = int(input("Enter a value for y: "))

    if x <= 0 or y <= 0:
        print("Error: Only positive non-zero integers are allowed.")
    else:
        print(f"The LCM of {x} and {y} is = {lcm(x, y)}")

except ValueError:
    print("Error: Please enter valid integers.")