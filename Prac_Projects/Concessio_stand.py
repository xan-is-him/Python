#concession stand program

menu = {"pizza":300,
        "nachos":230,
        "popcorn":290,
        "fries":150,
        "pretzel":100,
        "chips":170,
        "soda":110,
        "lemonade":90,}

cart = []
total = 0

print("--------MENU--------")
for key,value in menu.items():
    print(f"{key:10}: Nrs{value:.2f}")
print("--------------------")

while True:
    food = input("What food do you want to buy?(q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your total is:  Nrs{total:.2f}")
print("--------------------")
