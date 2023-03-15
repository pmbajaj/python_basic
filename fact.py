a=int(input("Enter number to find factorial of : "))
f = int(1)
for i in range(1,a+1):
	f = f*i
print("Factorial of ",a,"is :",f)