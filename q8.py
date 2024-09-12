#Write a program to find the roots of a quadratic equation when the coefficients a, b and c are given ( assume that a, b and c are integers)
import math
a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
c=int(input("Enter value of c"))
d=b*b-(4*a*c)
if d==0:
    r1=-b/(2*a)
    r2=-b/(2*a)
elif d>0:
     r1=(-b+math.sqrt(d))/(2*a)
     r2=(-b-math.sqrt(d))/(2*a)
else:
    r1=-b/(2*a)
    r2=math.sqrt(-d)/(2*a)
print("Roots are= ",r1,"and ",r2)    
