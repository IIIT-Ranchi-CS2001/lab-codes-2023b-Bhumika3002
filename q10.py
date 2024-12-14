#Write a python script to find the sum of the digits of the given number using a while loop. Display the number and the sum.

n =int(input("Enter a no : "))
s=0
while n!=0:
    r=n%10
    s=s+r
    n=n//10
print("Number=",n) 
print("Sum=",s)    
