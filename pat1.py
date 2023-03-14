def pattern():
     n = int(input("Enter the number of rows you want in the pattern : "))
     for i in range(1,n+1):
          for j in range(1,i+1):
               print("* ",end="")
          print("\r")
         
     for i in range(1,n+1):
          for j in range(65,65 + i):
               print(chr(j)," ",end="")
          print("\r")
         
     z = 65
     for i in range(0,n+1):
          for j in range(0,i+1):
               print(chr(z)," ",end="")
               z = z+1
          print("\r")
     
pattern()
print("A star pattern was printed.")
print("A pattern with alphabets was printed.")