'''
print("Hello World!")
print()
# This is a comment. I can write whatever I want
# Here and it won't do anything about it.
# It has no effect on the code.
print()  # This adds extra spaces on the terminal.
print("This will print here. Notice the spacing.")

a=4
b=3
print(a + b)
print(a * 5)
print(5 - 3)
print(6 / 5)  # Results in a float (with decimals)

print("Figure this out")
print(6 // 4)  # Results in a integer (without decimals)
print(12 // 3)
print(9 // 4)

# more math stuff
print("Figure this stuff out too...")
print(6 % 4)
print(5 % 3)
print(9 % 4)


# Variables
car_name = "The Wiebe Mobile"
car_type = "Tesla"
car_cylinders = 1024
car_miles_per_gallon = 0.01

print("I have a car called %s. It's pretty nice." % car_name)

# Input
# name = input ("What is your name? ")
# print("Hello %s" % name)

# Auto - comment - Ctrl + /
# age = input("How old are you? ")
# print("%s?! You belong in a museum." % age)

# Hidden age
real_age = input("How old are you? >_")
hidden_age = real_age + 5

print(hidden_age)
print("%d is incredibly old." % (hidden_age, real_age))
'''

# functions
def printHelloWorld ():
    print("Hello World!")

printHelloWorld()
'''
This is a multi-line comment
I can type anywhere here
'''


# f(x) = 2x + 3
def f(x) :
    print(2*x + 3)


f(1)
f(5)
f(5000)

# Loops
for i in {1, 2, 3}:
    printHelloWorld()

print()
for i in range (3) :
    printHelloWorld()

print()
for i in range(5):  # Range starts at 0 and goes to 4
    f(i)

for i in range(5):
    print(i**2)


# While loops
a = 0
while a < 10:
    print(a)
    a += 1 # This is the same thing as a = a + 1

'''
Hints with loops:
for loops - Use when you know exactly how many 
While loops - Use when you DON'T know how many iterations
'''

# Random numbers
import random  # This should always be on line 1
print(random.randint(0, 100))


# Control Statements
def grade_calc(percentage):
    if percentage >=90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


print(grade_calc(82))

# Equality Statements
print(5 > 3)
print(5 >=3)
print(3 == 3)
print(3!= 4)
"""
a = 3 # A is set to 3
a == 3 # Is a equal to 3?
"""






















