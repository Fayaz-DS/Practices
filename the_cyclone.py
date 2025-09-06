height = 130
credits = 120

height = int(input("Enter your height in cm:"))
credits = int(input("Enter your credits:"))

if height > 120 and credits > 110:
    print("You can ride the rollercoaster")
elif height < 120 and credits > 110:
    print("You do not have the required height to ride the rollercoaster")
elif height > 120 and credits < 110:
    print("You do not have the required credits to ride the rollercoaster")
else:
    print("You do not have the required height and credits to ride the rollercoaster")