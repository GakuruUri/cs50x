# try and except

# ValueError: invalid literal for int() with base 10: 'cat'
# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")


# # The below has an error in order of operation
# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
    
# print(f"x is {x}")


# Try except supports also

# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")


# Add a loop so that the program prompts again and again
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
    
# print(f"x is {x}")


# Option 2 without an else
# while True:
#     try:
#         x = int(input("What's x? "))
#         break
#     except ValueError:
#         print("x is not an integer")
        
# print(f"x is {x}")


# Create a function

# def main():
#     x = get_int()
#     print(f"x is {x}")


# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break
        
#     return x

# main()
            


# def main():
#     x = get_int()
#     print(f"x is {x}")
    
# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         # else:
#         #     return x
        
# main()
        
# Pass keyword

# def main():
#     x = get_int()
#     print(f"x is {x}")
    
# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             pass

# main()



# Making the code more dynamic

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")
    
    
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
        
main()

