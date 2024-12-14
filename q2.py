#WAP to find area and perimeter using Heron's formula
#Find all three angles of triangle
import math 

a=int(input("Enter first side"))
b=int(input("Enter second side"))
c=int(input("Enter third side"))
p=(a+b+c)
s=p/2
x=s*(s-a)*(s-b)*(s-c)
print("Perimeter:",p)
print("Area:",math.sqrt(x))
print("First Angle:",math.degrees((math.acos((b**2+c**2-a**2)/(2*b*c)))))
print("Second Angle:",math.degrees((math.acos((a**2+c**2-b**2)/(2*a*c)))))
print("Third Angle:",math.degrees((math.acos((b**2+a**2-c**2)/(2*a*b)))))
