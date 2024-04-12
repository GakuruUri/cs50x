# x = float(input("What's x? "))
# y = float(input("What's y? "))

# Rounding off and printing using and f-string
# z = round(x + y)
# print(f"{z:,}")

# Division
# z = round(x / y, 2)
# print(z)


# z = x / y
# print(f"{z:.3f}")

def main():
    x = int(input("What's x? "))
    print("x squared is:", square(x))

def square(n):
    # return n * n   
    # return pow(n, 3)
    return n ** 4

main()