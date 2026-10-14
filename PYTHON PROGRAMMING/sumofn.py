list1=[]
n=int(input("enter the number of elements in the list:"))
print("enter elements in the list:")
for i in range(n):
    value=int(input())
    list1.append(value)
total=0
for num in list1:
    total=total+int(num)
print("sum=",total)
