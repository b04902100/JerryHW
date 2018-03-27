def calculator(num1, num2, operator):
	def add(num1, num2): return (num1+num2)
	def substract(num1, num2): return (num1-num2)
	def multiply(num1, num2): return (num1*num2)
	def divide(num1, num2): return (num1/num2)

	if operator == '+': print(num1,"+",num2,"=", add(num1,num2))
	elif operator == '-': print(num1,"-",num2,"=", subtract(num1,num2))
	elif operator == '*': print(num1,"*",num2,"=", multiply(num1,num2))
	elif operator == '/': print(num1,"/",num2,"=", divide(num1,num2))
	else: print("invalid")

	return