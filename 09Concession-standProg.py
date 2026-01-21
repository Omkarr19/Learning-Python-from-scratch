# Concession stand program
# dictionary {key:value}
# get() - used to retrieve the value for a specified key
#demo of menu.items()
#menu = {"pizza" : 60, "burger" : 80, "Vadapav" : 20, "Samosa" : 25}
#print(menu.get("Samosa"))  # This will print value of samosa
#for i, x in menu.items() : 
#    print(f"{i} : {x}")   # i = all keys and x = all values


menu = {"pizza" : 3.00,
        "nachos" : 4.50,
        "popcorn" : 6.00,
        "fries" : 2.50,
        "chips" : 1.00,
        "pretzel" : 3.50,
        "soda" : 3.00,
        "lemonade" : 4.25}

cart = []
total = 0

for key, value in menu.items() :   #menu.items() return key-value pair,   here first variable (key) assigned to all keys in dict and (value) assigned to all values
    print(f"{key :10} : {value:.2f}")

while True :
    food = input("select an item (q to quit): ")
    if food.lower() == "q" :
        break
    elif menu.get(food) is not None : #menu.get(food) will check if item entered by user is in a dict or not, and it is not there it returns "None"
        cart.append(food)

for food in cart :
    total += menu.get(food)   #menu.get() will return values for each food item in List cart
    print(food, end = " ")

print()
print(f"Total is : ${total:.2f}")