n=int(input("Enter the number of terms:"))
a=0
b=1
print("The first",n,"numbers in the fibinocci series=")
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
