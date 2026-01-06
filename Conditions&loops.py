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

food = input("Enter your fav food (press 'q' to quit): ")
while not food.lower() == "q" :
    print(f"u fav food is {food}")
    food = input("Enter another your fav food (press 'q' to quit): ")
print("go away bye")