import random  #gives access to alot of useful methods involving random numbers
#random.randint(low, high) - returns random integer from given range
#random.random()           - returns random floating number between 0 and 1
#random.choice()           - selects random elements from collections (list, tupple, dictionary)
#random.shuffle()          - shuffles the collection in random order

#print(help(random))  #will return comprehensive list

#number = random.randint(1, 6)  #will return random number between 1-6
#print(number)

#can also write this way
#low = 1
#high = 100
#number = random.randint(low, high)  
#number = random.random()  # will return random floating number between 0 and 1
#print(number)


#options = ("rock", "paper", "scissors")
#selected = random.choice(options)
#print(selected)

#cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
#random.shuffle(cards)
#print(cards)