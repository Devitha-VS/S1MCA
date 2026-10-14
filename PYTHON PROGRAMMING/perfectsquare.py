number=[]
start=int(input("Enter a starting digit:"))
end=int(input("Enter a ending digit:"))
if start<1000 or end>9999 or start>end:
    print("invalid range of number")
else:
    for num in range(start,end+1):
        if num%2==0:
            root=int(num**0.5)
        if root*root==num:
            number.append(num)
print("Four digit even perfect squares in the given range is:")
print(number)
            
    
