import Scientific_Calculator
import os

os.system('cls' if os.name == 'nt' else 'clear')

while True:
	print("Select Operation.")
	print("1: Sqaure Root - √x")
	print("2: Factorial - x!")
	print("3: Natural Log - ln(x)")
	print("4: Power - x^y")
	print("e: Exit")
	
	operation = input("Enter your choice : ")
	
	if operation in ('1', '2', '3', '4'):
		num = float(input("Enter the number: "))
		
		if operation == '1':
			print("Answer : ", Scientific_Calculator.square_root(num))
			
		elif operation == '2':
			print("Answer : ", Scientific_Calculator.factorial(num))
		
		elif operation == '3':
			print("Answer : ", Scientific_Calculator.natural_log(num))
		
		elif operation == '4':
			exp = float(input("Enter the power : "))
			print("Answer : ", Scientific_Calculator.power(num, exp))
		# Not using Clear screen here as it will also clear the result as well
		# os.system('cls' if os.name == 'nt' else 'clear')
		
	elif operation == 'e' or 'E':
		break
		
	else:
		print("Please Enter a valid Input")
	print("\n")
	
