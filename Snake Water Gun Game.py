import random
computer=random.choice(['snake','water','gun'])
print("Welcome to the Snake-Water-Gun Game")
User=input("Enter your choice: ")
Lwr=User.lower()
def game(User,computer):
    if Lwr==computer:
        return "Tie"
    elif Lwr=='snake':
        if computer=='water':
            return "User wins"
        else:
            return "Computer wins"
    elif Lwr=='water':
        if computer=='gun':
            return "User wins"
        else:
            return "Computer wins"
    elif Lwr=='gun':
        if computer=='snake':
            return "User wins"
        else:
            return "Computer wins"
    else:
        return "Invalid Input"
print(f"Computer chose {computer}")
print(f"You chose {User}")
print(f"{game(User,computer)}")    
