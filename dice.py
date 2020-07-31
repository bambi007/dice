import random


while True:
    print("Roll a dice? (Y/N)")
    roll = input().upper()

    if roll == "Y":
        print("\nResult:", random.randint(1, 6), "and", random.randint(1, 6))

    elif roll == "N":
        print("\nSee you later!")
        break

    else:
        print("\nInvalid answer, try again.")
