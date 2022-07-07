#Write a program to swap 2 numbers using third variable.

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

c=a
a=b
b=c

print("The value of a after swapping : ",a)
print("The value of b after swapping : ",b)