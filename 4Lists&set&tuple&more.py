#collection = single "variable"  used to store multiple values
# List =  [] ordered and changeable. Duplicates OK
# Set =   {} unordered and immutable(cannot be changed), Add/remove OK, NO Duplicates, dislpayed in random order
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER 

#fruits = ["apple","banana","orange","coconut"]
#print(fruits)

#can use the index operator [index_number] to print specific element
#planets = ["Earth", "Venus","Mars"]
#print(planets[1])
#print(planets[::2])
#print(planets[1:3])
#print(planets[::-1])

#for planet in planets:
#    print(planet)

#if you need description of all methods and attributes use "help" method
#print(help(planets))
#print(dir(planets)) #The dir() function in Python is a powerful, built-in tool for inspecting objects and listing the names of valid attributes and methods associated with them

#print(len(planets))  #displays length

#print("uranus" in planets)  #checks if that element is in list & return true or false 

#we can replace a element at specific index also
#planets[0] = "Jupyter"
#for planet in planets:
#    print(planet)

#we can add element at the end of the list using append keyword
#planets.append("Jupyter")
#print(planets)

#remove method to remove element
#planets.remove("Earth")

#add at perticular position using insert method
#planets.insert(2, "Jupyter")

#to sort in alphabetical order user sort() method and reverse using reverse() method
#planets.sort()
#planets.reverse()

#to clear elements use clear method
#planets.clear()

#to print index of element
#print(planets.index("Earth"))

#to count if an elements occurs multiple time use count() method
#print(planets.count("Earth")) 

#fruits = {"apples","orange","banana","coconut"}
#print(dir(fruits))

#mostly have same attrbutes as List like len(), or we can check if element is in set using ("element" in set_name) - return true, false , index operator
# can add elements using add() method
#fruits.add("pineapple") 
#fruits.remove("pineapple")
#fruits.pop()  #this will remove first element of set, but it is going to be random
#fruits.clear()
#print(fruits)

#its = ("apple","orange","banana","coconut","coconut")
#mostly have same attrbutes as List like len(), or we can check if element is in set using ("element" in set_name) - return true, false , index operator
#print(fruits.count("coconut"))