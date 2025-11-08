'''print("I'm Gonna be the best out there!");

#variable = A container for a value (String,Integer,float,boolean)
#           A variable behaves as if it was value it contains

First_name = "BikyaJackstron"
Food = "Biryani"
email = "bokya19omkar@gmail.com"

print(First_name)
print(f"Hello {First_name}")       
print(f"You Like {Food}")
print(f"Your email is {email}");

#Integers
age = 25
quantity = 3
num_of_students = 30
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#Float
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"My gpa is {gpa}")
print(f"You ran {distance}km")

#boolean
is_student = True

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")


#Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()
name = "BikyaJackstron"
age = 19
gpa = 3.2
is_student = True

print(type(name))
print(type(age))

#converting gpa into int
gpa = int(gpa)
print(gpa)

#converting age in float
age = float(age)
print(age)

#converting age in str
age = str(age)
print(age, type(age))

age += "1" #using double quate cuz age is string now this is strong concat
print(age)

#converting str in bool
# gives true is str has value, false if empty str
name = bool(name)
print(name)
'''

