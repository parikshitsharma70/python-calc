#!/usr/bin/env python

#NoCopyrightCode --- Feel free to use and distribute

#Author : Parikshit Sharma

#Interactive Python Calculator



while True:
	print("-----------Welcome to the Interactive Python Calculator----------- ")
	print("This calculator includes a bunch of functionalities which can be accessed by entering an option \n \n")
	print("Options: \n \n")
	print("Enter 'add' to perform addition of two or numbers")
	print("Enter 'subtract' to perform subtraction of two numbers")
	print("Enter 'mutliply' to perform multiplication of two numbers")
	print("Enter 'divide' to perform division of two numbers")
	print("Enter 'exp' to perform exponential function between two numbers")
	print("Enter 'modulo' to perform modulo function between two numbers")
	print("Enter 'floor' to perform floor division between two numbers")
	print("Enter 'quit' to end the program \n \n")

	user_input = input("Enter your option with quotes:  ")


	if user_input == "quit":
		break
	elif user_input == "add":
		print("Enter the two numbers to be added")
		x = float(input("Enter a number:  "))
		y = float(input("Enter a number:  "))
		result = str(x+y)
		print("The answer is " + result)
	elif user_input == "subtract":
		print("Enter the two numbers to be subtracted")
		x = float(input("Enter a number:  "))
		y = float(input("Enter a number:  "))
		result = str(x-y)
		print("The answer is "+ result)
	elif user_input == "multiply":
		print("Enter the two numbers to be multiplied")
		x = float(input("Enter a number:  "))
		y = float(input("Enter a number:  "))
		result = str(x*y)
		print("The answer is "+ result)
	elif user_input == "divide":
		print("Enter the two numbers to be divided")
		x = float(input("Enter a number:  "))
		y = float(input("Enter a number:  "))
		result = str(x/y)
		print("The answer is "+ result)
	elif user_input == "exp":
		print("Enter the base and the power in that order")
		x = float(input("Enter a number:  "))
		y = float(input("Enter a number:  "))
		result = str(x**y)
		print("The answer is "+ result)
	elif user_input == "modulo"
		print("Enter the two operands in that order")
		x = float(input("Enter a number:  "))
		y = float(input("Enter a number:  "))
		result = str(x%y)
		print("The answer is "+ result)
	elif user_input == "floor"
		print("Enter the two operands in that order")
		x = float(input("Enter a number:  "))
		y = float(input("Enter a number:  "))
		result = str(x//y)
		print("The answer is "+ result)
	else:
		print("Please enter a valid input")
