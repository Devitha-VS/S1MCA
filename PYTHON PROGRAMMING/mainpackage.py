import graphics.rectangle
import graphics.circle
l=int(input("enter the length of the rectangle:"))
b=int(input("enter the breadth of the rectangle:"))
r=int(input("enter the radius of circle:"))
print("area of rectangle=",graphics.rectangle.rect_area(l,b))
print("primeter of rectangle=",graphics.rectangle.rect_perimeter(l,b))
print("area of circle=",graphics.circle.circle_area(r))
print("perimeter of circle=",graphics.circle.circle_perimeter(r))
from graphics._3Dgraphics import cuboid
from graphics._3Dgraphics import sphere
l1=int(input("enter the length of cuboid:"))
b1=int(input("enter the breadth of cuboid:"))
h1=int(input("enter the height of the cuboid:"))
r1=int(input("enter the radius of sphere:"))
print("volume of cuboid=",graphics._3Dgraphics.cuboid.cuboid_volume(l1,b1,h1))
print("area of sphere=",graphics._3Dgraphics.sphere.sphere_area(r1))
      
