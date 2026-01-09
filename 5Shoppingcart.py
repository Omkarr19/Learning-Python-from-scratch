# Shopping cart program

foods = []
prices = []
total = 0

while True :    #we will need something to break loop which we will add later 
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break   #breaks while loop
    else :
        price = int(input(f"Enter price of a {food}: $"))
        foods.append(food)   #to store user's food in list
        prices.append(price)

print("-------- YOUR CART ---------")
for food in foods:  
    print(food, end = ",")
for price in prices:
    total += price

print(f"Your total is: ${total}")

#print("-------- YOUR CART ---------")
#for food,price in foods,prices:   #you can write both lists or any variable in for loop using ","
#    print(food, price, end = " ")

# Or we can use zip method

#list1 = ['apple', 'banana', 'cherry', 'orange']
#list2 = ['red', 'yellow', 'red', 'orange']

# Use zip to iterate over both lists simultaneously
#for item1, item2 in zip(list1, list2):
#    print(item1, item2)   