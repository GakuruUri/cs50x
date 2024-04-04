# argument vector
import sys

# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# Check for errors
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
#     # print("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
#     # print("Too many arguments")
# # else:
# #     print("Hello, my name is", sys.argv[1])

# # Print name tags
# print("hello, my name is".title(), sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
