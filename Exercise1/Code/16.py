'''Take starting number and ending number from the user and print following series.
Output :-
Enter starting number : 30
Enter ending number : 0
30
27
24
21
18
15
12
9
6
3
0'''

a=int(input("Enter the starting number: "))
b=int(input("Enter the ending number: "))

for i in range(a,-1,-3):
 print(i)