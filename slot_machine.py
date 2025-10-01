import random

def spin_slot_machine():
    symbols = ['Cherry', 'berry', 'Watermelon', 'Seven']
    return [random.choice(symbols) for _ in range(3)]
result = spin_slot_machine()
if result[0] == result[1] == result[2]:
    print(result[0], '|', result[1], '|', result[2])
    print("Jackpot! You win!")
else:
    print(result[0], '|', result[1], '|', result[2])
    print("Try again!")

while result[0] != result[1] or result[1] != result[2]:
    user_input = input("Enter 'spin' to try again or 'end' to quit: ")
    result = spin_slot_machine()
    if user_input == 'spin':
        print(result[0], '|', result[1], '|', result[2])
    elif user_input == 'end':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input, please enter 'spin' or 'end'.")
    
