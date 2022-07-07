'''Take a number check if a number is less than 100 or not. If it is less than 100
 then check if it is odd or even.'''

x=int(input("Enter a number : "))

if x<100:

 print(x, "is less than 100")
 if x%2==0:
     print(x, "is an even number")
 else:
     print(x, "is an odd number")

else:
 print(x, "is not less than 100")