#Take a number and check whether it is zero, positive or negative.

x=int(input("Enter any integer: "))

if x>=0:
    if x==0:
     print(x, "is zero")

    else:
     print(x, "is a positive number")

else:
 print(x, "is a negative number")