
###
# A program that calculates the sum of two numbers.
# Modify the program to calculate the sum of three numbers.
# task 1
# number1 = 71
# number2 = 14
# number3 = 21
# result = number1 + number2 + number3
# print('Number 1: ', number1)
# print('Number 2: ', number2)
# print('Number 3: ', number3)
# print('The result of summation: ', result)
#task 2
# 1. Two variables x and y have values of 7 and 34. Write a program that swaps variable values (x should be 34 and y should be 7). Use an additional, auxiliary variable.

#     > Hint: It is a good idea to always put a short description of the program in a comment at the beginning of the file. You can use the task text for this.

#     > Hint: The program file name may contain the section number and task number, e.g. 3-7.py.


###
# A program for swapping two varable values
#
# x = 7
# y = 34
# z = 0 
# print("Before swapping: x=", x, "y=", y)
# z = x
# x = y
# print("After swapping: x=", z, "y=", x)
#task 3
# 1. Write a program that, for a given speed in km/h, prints the speed in m/s.

###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
# speed_kmh = 70
# speed_ms = speed_kmh/3600
# print(speed_kmh, "km/h = ", speed_ms, "m/s")
#task 4
# 1. Write a program that calculates the length of the diagonal of a rectangle with sides a=5 and b=8. To calculate the square root of a given value, use the sqrt function. The function is available in a module called math, which you must import into your program.
###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
# import math
# a = 5
# b = ...
# diagonal = math.sqrt(a**2+b**2)
# print(f"Length of diagonal of the rectangle with sides a:{a} and b:{b} equals {diagonal}")
#task 5
# 1. The distance to the horizon depends on the height of the observer above the ground. The higher you are, the farther away the horizon is. For most situations, you can use the following formula:

# d = 3.57 × √h

# Where:

# * d is the distance to the horizon in kilometers
# * h is the height of the observer in meters

# Write a program that calculates the distance to the horizon from a height given in meters from the keyboard. Then, using the program, calculate the distance to the horizon in km when:

# 1. You are standing on a beach, by the sea, on the water line (calculate the distance for your height in m). You have probably been to the seaside many times. Can you believe that the horizon is only a few kilometers away?
# 1. You are looking out of a hotel window located by the sea, the window is at a height of 20 meters.
# import math
# meters = int(input("Enter height:"))
# distance = 3.57*math.sqrt(meters)
# print(distance)
#task 6
# In the year 2022, the world population was approximately 8 billion. The Northern Hemisphere has 7.2 billion people. Write a program that calculates and prints:
# The number of people and percentage of the total population living in the Northern Hemisphere
# The number of people and percentage of the total population living in the Southern Hemisphere


###
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#
# total = 8000000000
# north = 7200000000
# south = total-north
# print("World population: ", total)
# print("Northern Hemisphere: ", north)
# print("Northern Hemisphere in %: ", north/total*100)
# print("Southern Hemisphere in %:", south/total*100)
#task 7
# The following program calculates and prints the average grade of a student, but it contains several errors. Fix the program so that it works correctly.


###
# A program that calculates and prints
# the average grade of a student
#
# math = 5
# art = 4
# music = 5
# history = 3
# average = math + art + music + history / 4
# print("Average grade is", average)
# One of the basic functionalities of a computer program is printing results on the computer screen. To print the results in a readable form, string (text) formatting available in programming languages is often used. In Python, it is called f-strings.

# <https://www.pythontutorial.net/python-basics/python-f-strings/>
    
# <https://docs.python.org/3/tutorial/inputoutput.html> 

# Below is a program for printing any text along with the value of a variable using f-strings:

###
# Printing student's personal data
#
# name = "Adam"
# age = 20
# height= 190
# future_age = age+6
# print(f"My name is {name}, I am {age} years old, and my height is {height} cm. In 6 years I will be {future_age}")
