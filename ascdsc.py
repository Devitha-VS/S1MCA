n=int(input("enter number of elements:"))
d={}
for i in range(n):
   key=int(input("enter key:"))
   value=input("enter value:")
   d[key]=value
asc=dict(sorted(d.items()))
desc=dict(sorted(d.items(),reverse=True))
print("Ascending order:",asc)
print("Descending order:",desc)
