# # print("Choose among the following shapes to calcualte the area: ")
# # print(" 1. Square")
# # print(" 2. Rectangle")
# # print(" 3. Triangle")
# # print(" 4. Circle")

# # shape = int(input("Enter the shape: "))

# # if shape == 1:
# #     side = float(input("Enter the side of the square in cm: "))
# #     area = side**2
# #     print(f"The are of the square is {area} cm^2")
# # elif shape == 2:
# #     length = float(input("Enter the length of the rectangle in cm: "))
# #     breadth = float(input("Enter the breadth of the rectangle in cm: "))
# #     area = length * breadth
# #     print(f"The area of the rectangle is {area} cm^2")
# # elif shape == 3:
# #     base = float(input("Enter the base of the triangle in cm: "))
# #     height = float(input("Enter the height of the triangle in cm: "))
# #     area = 0.5 * base * height
# #     print(f"The area of the triangle is {area} cm^2")
# # elif shape == 4:
# #     radius = float(input("Enter the radius of the circle in cm: "))
# #     area = 3.14 * radius**2
# #     print(f"The area of the circle is {area} cm^2")

# # while input("Do you want to calculate another area? (yes/no): ") == "yes":
# #     shape = int(input("Enter the shape: "))
# #     if shape == 1:
# #         side = float(input("Enter the side of the square in cm: "))
# #         area = side**2
# #         print(f"The are of the square is {area} cm^2")
# #     elif shape == 2:
# #         length = float(input("Enter the length of the rectangle in cm: "))
# #         breadth = float(input("Enter the breadth of the rectangle in cm: "))
# #         area = length * breadth
# #         print(f"The area of the rectangle is {area} cm^2")
# #     elif shape == 3:
# #         base = float(input("Enter the base of the triangle in cm: "))
# #         height = float(input("Enter the height of the triangle in cm: "))
# #         area = 0.5 * base * height
# #         print(f"The area of the triangle is {area} cm^2")
# #     elif shape == 4:
# #         radius = float(input("Enter the radius of the circle in cm: "))
# #         area = 3.14 * radius**2
# #         print(f"The area of the circle is {area} cm^2") 
# # else:
# #     print("Thank you for using the area calculator!")


# import random

# print("==================================================")
# print("Welcome to the rock, paper, and scissors Game!")
# print("==================================================")
# choices = ["rock", "paper", "scissors"]
# user_wins = 0
# computer_wins = 0
# rounds = int(input("Enter the number of rounds you want to play: "))
# for round in range(rounds):
#     user_choice = input("Enter your choice (rock, paper, scissors): ".lower())
#     computer_choice = random.choice(choices)
#     print(f"Computer chose: {computer_choice}")
#     if user_choice ==  computer_choice:
#         print("It's a tie!")
#     elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
#         print("You win")
#         user_wins += 1
#     else:
#         print("Computer wins!")
#         computer_wins += 1
# print(f"Score: You {user_wins}, Computer {computer_wins}")

# if user_wins > computer_wins:
#     print("Congratulations, you are the overall winner!")
# elif computer_wins > user_wins:
#     print("Computer is the overall winner! Better luck next time.")
# else:
#     print("It's an overall tie!")

print("==================================================")
print("Welcome to the dragon cave adventure game!")
print("==================================================")

print("You are standing at the entrance of a dark cave.")
print(" 1) Enter the cave")
print(" 2) Run away")
choice1 = input("What do you want to do? (1/2): ")
if choice1 == "1":
    print("You walk into the dark cave with barely any light.")
    print("After walking for a while, you start seeing two paths, because of the glowing stones on the walls.")
    print("The left path has a very bright glow, as if there is a cave full of gold. The right path has a dim glow.")
    print(" 1) Take the left path")
    print(" 2) Take the right path")
    choice2 = input("Which path do you want to take? (1/2):")
    if choice2 == "1":
        print("You walk down the left path, and you see a huge dragon sleeping on a pile of gold.")
        print(" 1) Try to steal some gold")
        print(" 2) Sneak past the dragon to the next room")
        choice3 = input("What do you want to do? (1/2): ")
        if choice3 == "1":
            print("As you try to steal some gold, the dragon wakes up and sees you.")
            print("The dragon is very angry and breathes fire at you.")
            print("You are burned to a crisp. Game over!")
        elif choice3 == "2":
            print("You sneak past the dragon and enter the next room.")
            print("You see a treasure chest filled with gold and jewels, and in the distance you see the exit.")
            print("Congratulations, you have found the treasure and won the game!")
    if choice2 == "2":
        print("You walk down the right path, and you encounter a golem, ready to wobble you up.")
        print(" 1) Fight the golem")
        print(" 2) Run away")
        choice4 = input("What do you want to do? (1/2): ")
        if choice4 == "1":
            print("You bravely fight the golem, but it is too strong.")
            print("You lost a lot of health, but barely managed to defeat the golem.")
            print("The golem drops a key, which you pick up.")
            print("You see a door in the distance, which you unlock with the key and escape the cave.")
            print("Congratulations, you have escaped the cave and won the game!")
        elif choice4 == "2":
            print("You run away from the golem, but you ran out of stamina.")
            print("The golem catches up to you and crushes you.")
            print("You got killed. Game over!")
if choice1 == "2":
    print("You run away from the cave, never knowing what could have been inside.")
    print("You live to see another day, but you will always wonder what was inside the cave.")
    print("Game over!")
