# speed_limit = 140
# car_speed = int( input('Enter car speed (km/h): ') )
# if car_speed>140:
#     print(f'Your speed is {car_speed}km/h')
#     print('Warning: speed limit exceeded!!')

# 1. A payment terminal in a store allows card payments. The customer has money in his bank account. The total value of purchases is given. The terminal prints a message whether the payment can be made or whether there are no funds in the customer's bank account. Write a program that acts as a payment terminal. Then, use the program and pay for the purchases below.

#     140, 499, 500, 501, 720 (for the last two amounts, there are no funds)

# account_balance = 500
# total_payment = int(input('Enter total payment:'))
#     if total_payment > account_balance:
#     print('Payment completed')
# else:
#     print('No funds')

# 1. A test is passed when the number of correctly completed tasks is at
#     least 50%. Write a program that checks whether the test is passed. Then use the program to check if you passed the test for the following number of properly performed tasks:

#     20, 11, 10, 9, 0 
###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
# total_tasks = 20
# tasks_ok = 20
# test_passed = False
    
# if tasks_ok >= total_tasks/2:
#     test_passed = True
    
# if test_passed:
#     print('Congratulations! You passed the test.')
# else:
#     print('Unfortunately, you failed the test.')

# Write a program that checks whether the number entered from the
#     keyboard is even or odd.
###
# Checking whether the number
# entered from the keyboard is even or odd 
#
# number = int(input('Enter number: '))
# if number%2==0:
#     print(f'{number} is even')
# else:
#     print(f'{number} is odd')

# The employee's basic salary is PLN 5000. The employee may receive a bonus of several percent of the basic salary. Write a program that calculates the employee's salary, taking into account the possibility of receiving a bonus. Then calculate the employee's total salary for the following cases:

#     * The employee does not receive a bonus
#     * The employee receives a bonus of 30%
###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
# basic_salary = 5000
# total_salary = 0
# is_bonus = True
# bonus = 0.15 
    
# if is_bonus==False:
#     total_salary = basic_salary
# else:
#     total_salary = basic_salary + basic_salary*0.15/100
# print(f'Basic salary: {basic_salary}')
# print(f'Bonus included? {is_bonus}')
# print(f'Total salary: {total_salary}')

# Clothing sizes are often labeled with letter symbols. Write a program that prompts the user to enter a clothing size and then prints a verbal description of the clothing size, as below.

#     * S: Small size
#     * M: Medium size
#     * L: Large size
#     * XL: Extra large size
#     * Incorrect symbol (if entered symbol dirrerent than S, M, L, XL)

#     Then check the correctness of the program for each of the size symbols.

###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
#
# size = input('Enter size symbol: ')

# if size == 'S':
#     print('S: Small size')
# elif size == 'M':
#     print('M: Medium size')
# elif size == 'L':
#     print('L: Large size')
# elif size == 'XL':
#     print('XL: Extra large size')
# else:
#     print('Incorrect symbol (if entered symbol dirrerent than S, M, L, XL)')

# The car has three driving modes: Auto (A), Manual (M) and Eco (E). In each of these three modes, the average fuel consumption in liters per 100 km is 7, 9 and 6 respectively. Write a program that calculates total fuel consumption for a given distance in km and a given driving mode. Then, calculate the total fuel consumption for the following data:

#     * distance 200 km, driving mode M (the result should be 18 liters) 
#     * distance 400 km, driving mode A (the result should be 28 liters) 
#     * distance 350 km, driving mode E (the result should be 21 liters) 
    ###
    # The car has three driving modes: Auto (A), Manual (M) and Eco (E).
    # In each of these three modes, the average fuel consumption in liters
    # per 100 km is 7, 9 and 6 respectively. Write a program that calculates
    # total fuel consumption for a given distance in km and a given
    # driving mode.
    #
# driving_mode = input('Enter driving mode (A/M/E):')
# distance = int(input('Enter distance in km:'))
# if driving_mode == 'A':
#     fuel_consumption = 7
# elif driving_mode == 'M':
#     fuel_consumption = 9
# elif driving_mode == 'E':
#     fuel_consumption = 6
# else:
#     print('You have entered a wrong driving mode. Try again.')
# total_consumption = distance/100 + fuel_consumption
# print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')

# Write a program that acts as a simple calculator. The program asks the user to enter a symbol of mathematical operation (+, -, *, /) and two numbers. The program should perform the appropriate mathematical operation on the given numbers and return the result. Then, using the program, calculate:

#     * 2 + 3
#     * 2 * 4
#     * 3 - 5
#     * 5 * 6

###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
# number1 = int(input('Enter a first number:'))
# number2 = int(input('Enter a second number:'))
# operator = input('Enter an operator:')

# if operator == '+':
#     print(number1+number2)
# elif operator == '-':
#     print(number1-number2)
# elif operator == '*':
#     print(number1*number2)
# elif operator == '/':
#     print(f'{number1/number2}')
# else:
#     print('Incorrect operator. Please try again.')

# Write a program that calculates and prints the quarter of the year for a given month number (1..12). Then check the program's results for the months:

#     12, 10, 9, 1

###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
# month = int(input('Enter month number (1..12): '))

# if month >= 10:
#     quarter = 4
# elif 6 < month < 9:
#     quarter = 3
# elif 3 < month < 6:
#     quarter = 2
# elif month <= 3:
#     quarter = 1
# print(f'Month {month} is in quarter {quarter}')

# 1. Write a program that checks what number was entered from the keyboard and prints one of the messages below. Then run the program and check the following numbers:

#     7, 1 ,0 ,-1 , -4

#     * Number ... is positive
#     * Number ... is negative
#     * Number is 0

# number = int(input('Enter a number:'))
# if number < 0: 
#     print (f'{number} is negative.')
# if number == 0:
#     print(f'{number} is 0.')
# if number > 0:
#     print(f'{number} is positive.')

# 1. Write a program that checks whether the entered login and password are correct.

###
# Checking login and password
#
# login = 'joe'
# password = 'abcd'
# entered_login = input('Login: ')
# entered_password = input('Password: ')
# if login == entered_login and password == entered_password:
#     print('You are logged in')
# else:
#     print('Incorrect login or password!!')

# The discount is available to children under 18, or people 65 or older. Write a program that checks whether a person of a given age is eligible for the discount. Then use the program to check if people of the age listed below are eligible for a discount.

#     72, 65, 64, 18, 17

###
# Checking if discount is available
# The discount is available to children under 18,
# or people 65 or older.
#
# age = int(input('Enter your age: '))

# if age < 18 or age>65 :
#     print("The person is eligible for the discount.")
# else:
#     print("The person is not eligible for the discount.")

# A user enters two integer numbers from the keyboard. Write a program
#     that checks whether at least one of them is not negative.

###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
# x = int(input('Enter first number: '))
# y = int(input('Enter second number:'))
# if not x < 0 or not y <0:
#     print(f'At least one of the numbers {x} and {y} is not negative')

#  Write a program that calculates and prints the number of days in a given month (1..12). Assume that February always has 28 days.
###
# Calculates the number of days in a month
#
# month = int(input('Enter month number (1..12):'))
    
# if month==1 or month==3 or month ==5 or month == 7 or month == 8 or month == 10 or month == 12:
#     days = 31 
# elif month==4 or month == 6 or month == 9 or month == 11:
#     days = 30 
# elif month==2:
#     days = 28  
# print(f'Month {month} has {days} days')

# 1. Write a program that checks if the given day number of the month is correct. Then, run the program for the following data:

#     * month 3, day 17
#     * month 9, day 31
#     * month 2, day 30

###
# Checks if the given day number of the month is correct
#
# month = int(input('Enter month number (1..12): '))
# day = int(input('Enter the day number of the month: '))
# day_ok = False
    
# if month==1 or month==3 or month ==5 or month == 7 or month == 8 or month == 10 or month == 12:
#     if day >=1 and day <= 31:
#         day_ok = True
#     elif month== month==4 or month == 6 or month == 9 or month == 11:
#         if day >=1 and day <= 30:
#             day_ok = True
#     elif month==2:
#         if day >= 1 and day <=28:
#             day_ok = True
#     else: 
#         day_ok = False
# message = f'Day {day} for the month {month}'
# if day_ok:
#     print('Message is correct')
# else:
#     print('Message is incorrect')