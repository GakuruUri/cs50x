'''
def main():
    print("Hello, world!")
    print("This is CS50p")
        
main()
'''
"""
# Ask user for their name, remove whitespaces and capitalize name
name = input("What's your name? ").strip().title()

# Split user's name into first and last name
first, last = name.split(' ')

# Say hello to the user
print(f"Hello, {last}!")
# print("Hello,",name)
# print("Hello, " + name)
"""



def main():
    name = input("What's your name? ")
    hello(name)
    
def hello(to="world!"):
    print("Hello, ", to)


main()




