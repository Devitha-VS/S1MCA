n=int(input("enter number of elements in first dictionary:"))
d1={}
for i in range(n):
      key=int(input("enter key:"))
      value=input("enter value:")
      d1[key]=value
n1=int(input("enter number of elements in second dictionary:"))
d2={}
for i in range(n1):
       key=int(input("enter key:"))
       value=input("enter value:")
       d2[key]=value
merged={**d1,**d2}
print("Dictionary1:",d1)
print("Dictionry2:",d2)
print("Merged Dictionary:",merged)
