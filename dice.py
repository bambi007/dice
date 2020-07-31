import random

# This is a simple dice rolling simulator

print("roll a dice")


def roll():
    random_number = random.randint(1, 6)
    print(random_number)


roll()

print("Another turn? (Y/N)")
action = str(input())
action.upper()



if action == "Y":
    roll()


elif action == "N":
    exit

else:
    print("invalid input, try again")
    action = str(input())
