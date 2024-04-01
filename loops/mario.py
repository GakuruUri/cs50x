# print("#")
# print("#")
# print("#")


# for _ in range(3):
#     print("#")


# def main():
#     print_column(3)
    
    
# def print_column(height):
#     for _ in range(height):
#         print("#")
        
# main()  


# def main():
#     print_row(4)
    
    
# def print_row(width):
#     print("?" * width)
    
# main()


def main():
    print_square(3)
    
  
# Option 1   
# def print_square(size):
# # For each row in square
#     for i in range(size):
# # for each row in row
#         for j in range(size):
# # print brick
#             print("#", end="")
# # This prints a new black line
#         print()


#option 2
# def print_square(size):
#     for i in range(size):
#         print("#" * size)
# main()


# Option 3
def print_square(size):
    for i in range(size):
        print_row(size)
        
        
def print_row(width):
    print("#" * width)
    
main()
