#Write a program to swap 2 numbers without taking third variable.

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

a=a+b
b=a-b
a=a-b

print("The value of a after swapping : ",a)
print("The value of b after swapping : ",b)