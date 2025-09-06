# Write code below 💖
rating = float(input("Enter your rating: "))


if rating > float(4.5):
  print("Extraordinary")
elif rating > 4 and rating <= 4.5:
  print("Excellent")
elif rating > 3 and rating <= 4:
  print("Good")
elif rating > 2 and rating <= 3:
  print("Fair")
else:
  print("poor")

