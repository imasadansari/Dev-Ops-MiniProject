import math

# Functions For the operations

def square_root(num):
	# GEtting Exception in case of taking sqare root of Negative numbers
	if num >= 0:
		num = math.sqrt(num)
		return num
	else:
		# Prevent Exception : ValueError: math domain error
		# Occured due to taking sqare root of negative numeber
		# num == num
		print("Cannot calculate Sqaure root of Negative numbers")
		return float(num)

	
def factorial(num):
	temp = float(num)
	# TO prevent ValueError: factorial() not defined for negative values EXCEPTION
	if temp >= 0:
		# print(temp, "    ", round(temp))
		if temp == float(round(temp)):
			temp = math.factorial(float(temp))
		else:
			temp = round(temp)
			print("Cannot take Factorial of Decimal Numbers, SO we converted It to INT")		
	else: 
		temp = 0.0
		print("Factorial of negative number cannot be taken")
	return temp


def natural_log(num):
	temp = float(num)
	
	if(temp > 0):
		temp = math.log(float(temp))
		#return temp
	else:
		temp = 0
	return temp


def power(num1, num2):
	return (num1 ** num2)


