#Write a python script to find the squares of first n natural numbers. Display both the number and the square as shown below. Use while loop

n=int(input("Enter no upto which square is to be found : "))
i=1
print("Number Square")
while i<=n:
    print(i,"    ",i*i)
    i=i+1
