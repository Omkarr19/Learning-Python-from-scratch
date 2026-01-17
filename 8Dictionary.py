# dictionary = a collection of {key : value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA" : "Washington D.C.",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Russia" : "Moscow"}

#print(dir(capitals))
#print(help(capitals))

#print(capitals.get("India"))

#if capitals.get("Japan") :
#    print("The capital exists")
#else :
#    print("The capital doesn't exist")

#capitals.update({"Germany" : "Berlin"})
#capitals.update({"USA" : "Detroit"})
#capitals.pop("China")
#capitals.popitem()   #removes latest element from dictionary
#capitals.clear()

#keys = capitals.keys()  #will return all the keys
#for key in capitals.keys():
#   print(key)

#values = capitals.values()
#for i in capitals.values():
#    print(i)

items = capitals.items  #reassembles a 2D list of Tuples.  O/P :- ([('USA','Washington D.C.'),('India', 'New Delhi'),('China', 'Beijing')])
for key, value in capitals.items():
    print(f"{key} : {value}")