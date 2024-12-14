#Write a python script to print the multiplication table of a given number up to the specified limit using a for loop.

n=int(input("Enter no for which multiplication table is to be printed"))
l=int(input("Enter limit upto which table is to be printed"))
i=1
for i in range(1,l+1):
    print(i*n)