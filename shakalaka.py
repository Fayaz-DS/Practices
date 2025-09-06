print("================================================")
print("              The sorting hat")
print("================================================")
print("                                       ")
print("Welcome to Hogwarts. We are now going to sort you into your house.")
print("Please answer the following questions by selecting 1 or 2.")

Gryffindor = 0
Hufflepuff = 0
Ravenclaw = 0
Slytherin = 0

print("Q1. Do you like Dawn or Dusk?")
print(" 1) Dawn")
print(" 2) Dusk")
answer1 = input("Choose 1 or 2: ")
if answer1 == "1":
    Gryffindor += 1
    Hufflepuff += 1
elif answer1 == "2":
    Ravenclaw += 1
    Slytherin += 1
else:
    print("Invalid input. Please select 1 or 2.")

print("                                       ")

print("Gryffindor =", Gryffindor,
      "Hufflepuff =", Hufflepuff,
      "Ravenclaw =", Ravenclaw,
      "Slytherin =", Slytherin)

print("Question 2. When I'm dead, I want people to remember me as: ")
print(" 1) The Good")
print(" 2) The Great")  
print(" 3) The Wise")
print(" 4) The Bold")   
answer2 = input("Choose 1, 2, 3 or 4: ")
if answer2 == "1":
    Gryffindor += 2
elif answer2 == "2":
    Slytherin += 2
elif answer2 == "3":
    Ravenclaw += 2
elif answer2 == "4":
    Hufflepuff += 2
else:
    print("Invalid input. Please select 1, 2, 3 or 4.")
print("                                       ")
print("Gryffindor =", Gryffindor,
      "Hufflepuff =", Hufflepuff,
      "Ravenclaw =", Ravenclaw,
      "Slytherin =", Slytherin)

print("Question 3. Which kind of instrument most pleases your ear?")
print(" 1) The violin")
print(" 2) The trumpet")
print(" 3) The piano")
print(" 4) The drum")
answer3 = input("Choose 1, 2, 3 or 4: ")
if answer3 == "1":
    Slytherin += 3
elif answer3 == "2":
    Hufflepuff += 3
elif answer3 == "3":
    Ravenclaw += 3
elif answer3 == "4":
    Gryffindor += 3
else:
    print("Invalid input. Please select 1, 2, 3 or 4.")
print("                                       ")
print("Gryffindor =", Gryffindor,   
      "Hufflepuff =", Hufflepuff,
      "Ravenclaw =", Ravenclaw,
      "Slytherin =", Slytherin)
print("                                       ")
if (Gryffindor > Hufflepuff) and (Gryffindor > Ravenclaw) and (Gryffindor > Slytherin):
    print("You have been sorted into Gryffindor")
elif (Hufflepuff > Gryffindor) and (Hufflepuff > Ravenclaw) and (Hufflepuff > Slytherin):
    print("You have been sorted into Hufflepuff")   
elif (Ravenclaw > Gryffindor) and (Ravenclaw > Hufflepuff) and (Ravenclaw > Slytherin):
    print("You have been sorted into Ravenclaw")
elif (Slytherin > Gryffindor) and (Slytherin > Hufflepuff) and (Slytherin > Ravenclaw):
    print("You have been sorted into Slytherin")
else:
    print("You have been sorted into Gryffindor, Hufflepuff, Ravenclaw and Slytherin")
print("                                       ")
print("================================================")
print("               End of the sorting hat")