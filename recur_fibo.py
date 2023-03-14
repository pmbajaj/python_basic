def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nt = int(input("Enter number of terms to be in the fibonacci series : "))
if nt <= 0:
     print("Please enter a positive integer")
else:
     print("Fibonacci sequence:")
     for i in range(nt):
          print(recur_fibo(i), "" ,end=" ")