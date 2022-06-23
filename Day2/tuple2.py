list1=[]
n=int(input("enter number"))
for i in range(0,n):
    element=input("enter value")
    list1.append(element)
tuple1=tuple(list1)
print(list1)
print(tuple1)