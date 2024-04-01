# print("meow")
# print("meow")
# print("meow")

# While loop
# i = 3
# while i != 0: # while i doesn't = 0
#     print("meow")
#     i = i -1 # decrease i by 1 each turn/loop
#     i -= 1 # decrease

# while loop Option 2
# i = 1
# while i <= 3:
#     print("meow")
#     i = i + 1 # increase i by 1 each turn/loop
#     i += 1 # increment    
# while loop Option 3


# i = 0
# while i < 3:
#     print("meow")
#     # i = i + 1 # increase i by 1 each turn/loop
#     i += 1  # increment


# for loop : Introduce lists
# for i in [0, 1, 2]:
#     print("meow")


# Add a range to the loop
# for i in range(3):
#     print("meow")

# since we are never using the varaible i there is a convention in python of using _
# for _ in range(3):
#     print("meow")
    

# print("meow\n" * 3, end="")

# Getting input from the user
# while True:
#     n = int(input("What's n? "))
#     if n < 0:
#         continue
#     else:
#         break


# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break
# for _ in range(n):
#     print("meow")


def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            #return n
            break
    return n
    
def meow(n):
    for _ in range(n):
        print("meow")
        
main()


