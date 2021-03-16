# Scientific Calculator functions
import math
import logging

logging.basicConfig(filename='Calculator.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

# Functions For the operations

def square_root(num):
	# GEtting Exception in case of taking sqare root of Negative numbers
	if num >= 0:
		ans = math.sqrt(num)
		logging.debug('Square Root of {} = {}'.format(num, ans))
		return ans
	else:
		# Prevent Exception : ValueError: math domain error
		# Occured due to taking sqare root of negative numeber
		# num == num
		print("Cannot calculate Sqaure root of Negative numbers")
		logging.debug('Square Root of {} = Cannot be caculated'.format(num))
		return float(num)
	
def factorial(num):
	temp = float(num)
	# TO prevent ValueError: factorial() not defined for negative values EXCEPTION
	if temp >= 0:
		# print(temp, "    ", round(temp))
		if temp == float(round(temp)):
			ans = math.factorial(float(temp))
			logging.debug('Factorial of {} = {}'.format(temp, ans))
		else:
			ans = round(temp)
			print("Cannot take Factorial of Decimal Numbers, SO we converted It to INT")		
			
			logging.debug('Factorial of {} = Cannot be calculated as it is Decimal number'.format(temp))
	else: 
		ans = 0.0
		print("Factorial of negative number cannot be taken")
		logging.debug('Factorial of {} = Cannot be taken as it is negative number'.format(num))
	return ans


def natural_log(num):
	temp = float(num)
	
	if(temp > 0):
		temp = math.log(float(temp))
		logging.debug('Natural Log of {} = {}'.format(num, temp))
		#return temp
	else:
		temp = 0
		logging.debug('Natural Log of {} = Cannot be taken as it is wither Zero or Negative number'.format(num))
	return temp


def power(num1, num2):
	ans = (num1 ** num2)
	logging.debug('{} to power of {} = {}'.format(num1, num2, ans))
	return ans


num1 = 225
num2 = 3
num3 = -4
num4 = 10

sqrt_result = square_root(num1)
logging.debug('Square Root of {} = {}'.format(num1, sqrt_result))

# Un-comment this block to get exception in log
# try:
#     fact_result = factorial(num3)
# except Exception as e:
#     logging.exception("Exception Occured")

fact_result = factorial(num4)
logging.debug('Factorial of {} = {}'.format(num4, fact_result))

ln_result = natural_log(num1)
logging.debug('Natural Log of {} = {}'.format(num1, ln_result))

pow_result = power(num1, num2)
logging.debug('{} Raised to Power {} = {}'.format(num2, num3, sqrt_result))

