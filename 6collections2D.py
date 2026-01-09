# 2D lists : just list made of lists
# 2dlist = [list1, list2, list3]

fruits = ["apple","orange","banana","coconut"]
vegetables = ["celery","carrots","potatoes"]
meats = ["chicken","fish","turkey"]

groceries = [fruits,vegetables,meats]
#print(fruits)
#print(vegetables)
#print(meats)
#print(groceries)
#print(groceries[2])  
#print(groceries[0][0])   #This will print element from 0th index list which is "fruits" and 0th index element which is "apple"

for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print()