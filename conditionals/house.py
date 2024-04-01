name = input("What's your name? ")


# if name == "Harry":
#     print("Griffindor")
# elif name == "Hermoiner":
#     print("Griffindor")
# elif name == "Ron":
#     print("Griffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who? ")

# if name == "Harry" or name == "Hermoine" or name == "Ron":
#     print("Griffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who? ")
    
    
# Match keyword    

# match name:
#     case "Harry":
#         print("Griffindor")
#     case "Hermoine":
#         print("Griffindor")
#     case "Ron":
#         print("Griffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who? ")


match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who? ")
