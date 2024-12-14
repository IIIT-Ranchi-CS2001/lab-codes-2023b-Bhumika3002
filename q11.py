#Write a python script to print the first n terms of the Fibonacci series using while loop

n=int(input("Enter the no of terms : "))
print("0 1 ",end="")
a=0
b=1
n=n-2
while n!=0:
    s=a+b
    print(s,end=" ")
    a=b
    b=s
    n=n-1





    