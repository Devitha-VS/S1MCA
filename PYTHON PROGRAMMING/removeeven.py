number=int(input("enter how many elements:"))
oddnum=[]
for n in range(number):
   oddnum.append(int(input("enter element:")))
for i in oddnum:
   if i%2==0:
      oddnum.remove(i)
print("list after removing even numbers:",oddnum)
