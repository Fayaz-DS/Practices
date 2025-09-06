weight = float(input("Enter your weight on earth: "))
planet = int(input("Choose a planet to know your weight there:\n1. Venus\n2. Mars\n3. Jupiter\n4. Saturn\n5. Uranus\n6. Neptune\n"))

if planet == 1:
    weight_venus = weight * 0.91
    print("Your weight on Venus is", weight_venus)
elif planet == 2:
    weight_mars = weight * 0.38
    print("Your weight on Mars is", weight_mars)
elif planet == 3:   
    weight_jupiter = weight * 2.34
    print("Your weight on Jupiter is", weight_jupiter)  
elif planet == 4:   
    weight_saturn = weight * 1.06
    print("Your weight on Saturn is", weight_saturn)        
elif planet == 5:
    weight_uranus = weight * 0.92
    print("Your weight on Uranus is", weight_uranus)
elif planet == 6:
    weight_neptune = weight * 1.19
    print("Your weight on Neptune is", weight_neptune)  
else:
    print("Invalid input")