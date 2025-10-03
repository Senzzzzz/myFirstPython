menu = {"POPCORN": 1.00,
        "HOT DOG": 2.00,
        "GIANT PRETZEL": 2.00,
        "ASST CANDY": 1.00,
        "SODA": 1.00,
        "BOTTLED WATER": 1.00}

cart = []
total = 0


for key, value in menu.items():
    print(f"{key:15}: ${value:.2f}")


while True:
    user = input("Select item (type q to finish): ")
    if user.lower() == "q":
        break
    elif menu.get(user) is not None:
        cart.append(user)

for item in cart:
    total += menu.get(item)

print(f"Your total is: ${total:.2f}")
