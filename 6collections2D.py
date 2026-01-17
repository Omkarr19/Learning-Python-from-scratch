# 2D lists : just list made of lists
# 2dlist = [list1, list2, list3]

#fruits = ["apple","orange","banana","coconut"]
#vegetables = ["celery","carrots","potatoes"]
#meats = ["chicken","fish","turkey"]

#groceries = [fruits,vegetables,meats]
#print(fruits)
#print(vegetables)
#print(meats)
#print(groceries)
#print(groceries[2])  
#print(groceries[0][0])   #This will print element from 0th index list which is "fruits" and 0th index element which is "apple"

#for collection in groceries: # This loop travels through all lists
#    for food in collection:  # This loop travels through elements from lists
#        print(food, end = " ")
#    print()



#making numpad using 2d Tuple   # not using set cuz it is unordered
num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()