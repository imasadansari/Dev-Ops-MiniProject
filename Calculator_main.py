import Scientific_Calculator

print("Select Operation.")
print("1: Sqaure Root - √x")
print("2: Factorial - x!")
print("3: Natural Log - ln(x)")
print("4: Power - x^y")

while True:
	operation = input("Enter your choice : ")
	
	if operation in ('1', '2', '3', '4'):
		num = float(input("Enter the number: "))
		
		if operation == '1':
			print(Scientific_Calculator.sqare_root(num))
			
		elif operation == '2':
			print(Scientific_Calculator.factorial(num))
		
		elif operation == '3':
			print(Scientific_Calculator.natural_log(num))
		
		elif operation == '4':
			exp = float(input("Enter the power"))
			print(Scientific_Calculator.power(num, exp))
		break
	else:
		print("Please Enter a valid Input")
