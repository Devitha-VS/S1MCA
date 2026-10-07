clr1=set(input("enter the colors of list1:").split(","))
clr2=set(input("enter the colors of list2:").split(","))
diff=list(clr1.difference(clr2))
print("colors not in list2:",diff)
