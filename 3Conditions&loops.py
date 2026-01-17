#if = So some code only if some condition is true else do something else
'''
age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up")
elif age <= 0:
    print("You haven't even born yet!")
else:
    print("Grow up lil bro")


#response = input("Would you like food (Y/N)? ")
#if response.lower() == "y":
#    print("Then Eat Dumbo!")
#elif response.lower() == "n":
#    print("Then don't eat dumbo!")
#else:
#    print("Choose something valid")

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter first operand: "))
num2 = float(input("Enter second operand: "))
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Enter valid operator")
print(f"You choose '{operator}' and your answer is {result}")


#Python Weight Converter
weight = float(input("Enter you Weight: "))
unit = input("Kilogram or Pounds? (K or L): ")

if unit.lower() == "k":
    weight = weight * 2.205
    unit = "Lbs."
elif unit.lower() == "l":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} was not valid")

print(f"Your weight is: {round(weight,2)} {unit}")

#temp converter
unit = input("Is this temp is Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temp: "))

if unit.lower() == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temp in Fahrenheit is: {temp}°F")
elif unit.lower() == "f":
    temp = round((temp - 32) * 5/9, 1)
    print(f"The temp in Celsius is: {temp}°C")
else:
    print(f"{unit} is not a valid unit")


# Logical operators = evaluate multiple conditions (or, and, not)
# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the conditions (not False, not True)

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")


#conditional expressions = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          x if condition else y

num = 6
# print("positive" if num > 0 else "negative")
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)


#String methods
#name = input("enter your full name: ")
phone_number = input("Enter your phone number: ")
#result = len(name)
#result = name.find(" ")
#result = name.rfind("o")  #r means reverse
#result = name.capitalize()
#result = name.upper()
#result = name.lower()
#result = name.isdigit()
#result = phone_number.count("-")
result = phone_number.replace("-" , " ")
print(result)
help(str)   # gives all string methods


#execise - validate user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

username = input("Enter your username: ")
if len(username) > 12:
    print("username should not be more than 12 characters")
elif not username.find(" ") == -1:
    print("Username should not contain any spaces")
elif not username.isalpha():                              # isalpha checks that string contains only letters or alphabets
    print("Username should not contain any digits")
else:
    print(f"Welcome {username}")


#indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

#credit_number = "1234-5678-9012-3456"
#last_digits = credit_number[-4:]
#print(credit_number[0])
#print(credit_number[0 : 4])   
#print(credit_number[ : 4])
#print(credit_number[5 :])
#print(credit_number[-1])
#print(credit_number[::2])
#print(credit_number[::-1])
#print(f"XXXX-XXXX-XXXX-{last_digits}")
'''

#format specifier = { value : flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = plce sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

#price1 = 30000.14159
#price2 = -987.65
#price3 = 12.34

#print(f"price 1 is {price1 :+,.2f}")
#print(f"price 2 is {price2 :-}")
#print(f"price 3 is {price3 : .3f}")


#WHILE LOOPS = execute some code WHILE some condition remains true

#here is simple if else example
#name = input("Enter your name: ")
#if name == "":
#    print("You did not enter your name")
#else:
#    print(f"Hello {name}")

#similar to that here is while loop example
#name = input("Enter your name: ")
#while name == "":
#    print("You did not enter your name")
#    name = input("please enter your name: ")     #this is neccessory to get our of the loop without this line it will be stuck in infinite loop
#print(f"Hello {name}")

#age = int(input("Enter your age: "))
#while age <= 0 :
#    print("Please Enter Valid age!")
#    age = int(input("Enter your age: "))
#print(f"You are {age} years old")

#food = input("Enter your fav food (press 'q' to quit): ")
#while not food.lower() == "q" :
#    print(f"u fav food is {food}")
#    food = input("Enter another your fav food (press 'q' to quit): ")
#print("go away bye") 

#num = int(input("Enter a number between 1 - 10: "))
#while num < 1 or num > 10 :
#    print("number is not between 1 - 10")
#    num = int(input("Enter a number between 1 - 10: "))
#print(f"your number is {num}")


#python compound interest calculator
#principle = 0
#rate = 0
#time = 0

#while principle <= 0:
#    principle = float(input("Enter principle amount: "))
#    if principle <= 0:
#        print("Principle amount can't be less than or equal to zero")

#while rate <= 0:
#    rate = float(input("Enter the interest rate: "))
#    if rate <= 0:
#        print("Interest rate can't be less than or equal to zero")

#while time <= 0:
#    time = int(input("Enter time in years: "))
#    if time <= 0:
#        print("Time in years can't be smaller than or equal to zero")

#print(f"principle amount is {principle}")
#print(f"Interest rate is {rate}%")
#print(f"Time in years is {principle}years")
#print("Calculating compound interest...")
#cm = principle * pow((1 + rate/100), time)

#print(f"balance after {time}year/s: ${cm: .2f}")

# for loops = execute a block of code a fixed number of times.
#             you can iterate over a range, string, sequence, etc.

#for i in range(1,11):    # 1 to 10
#    print(i)

#we can use reversed function too shown below
#for i in reversed(range(1, 11)):
#    print(i)
#print("HAPPYY NEWW YEARRR!!!")

# or also can be revesed as shown below!
# for i in range(11, 0, -1):
#       print(i)

#we can use one more parameter to display number by gaps
#for i in range(1, 11, 2):    #numbers will be displayed like (1,3,5,7,9) 
#    print(i)

#credit_card = "1234-5678-9012-3456"   #iteration over string

#for i in credit_card :
#    print(i)

#suppose we are counting from 1 to 20
#and i want to skip a number, then ill use "continue" keyword.
#if we use "break" keyword it will stop at 12
#for i in range(1, 21):
#    if i == 13:
#        continue
#    else :
#        print(i)


#COUNTDOWN TIMER USING SLEEP FUNCTION
#import time
#time.sleep(3)
#print("TIME'S UP")

#import time
#my_time = int(input("Enter your countdown time in seconds: "))
#for x in reversed(range(0, my_time)):
#    print(x)
#    time.sleep(1)
#print("TIME'S UP")

#import time
#my_time = int(input("Enter your time in seconds: "))
#for i in range(my_time, 0, -1): 
#    seconds = i % 60      # makes sure that seconds remain from 0 to 59
#    minutes = int(i / 60) % 60
#    hours = int(i / 3600)
#    print(f"{hours:02}:{minutes:02}:{seconds :02}")  #used format specifier for showing digits like 09 and not 9
#    time.sleep(1)
#print("Time's up")


#nested loop = A loop within another loop (outer, inner)
#              outer loop:
#                 inner loop:
# ex., while x>0:
#        while y>0:
#           print("Do something")

#import time
#for i in range(1,10):
#    print(i, end = " ")   #end keyword used to edit output format. here, default is end = "\n" which prints o/p in one below one, if we write end = " " then it will print in one line with space.
#    time.sleep(1)

#for x in range(3):  #whatever code will be in this loop will be executed 3 times
#    for y in range(1,10):
#        print(x, end = " ")

#Now, we have to pay attention to which loop we are printing in print statement
#here, with this same loops but let's print different loop this time

#for x in range(3):
#    for y in range(1,10):
#        print(y, end = "")
#this will print numbers from 1 to 9 three times.

#for x in range(3):
#    for y in range(1,10):
#        print(y, end = " ")
#    print()
#this will display numbers 1 to 9 in one line and then another set of 1 to 9 below it.

#now try to take some input
#rows  = int(input("Enter number of rows: "))
#columns = int(input("Enter number of columns: "))
#symbol = input("Enter symbol to print: ")

#for x in range(rows):
#    for y in range(columns):
#        print(symbol, end = "")
#    print()
