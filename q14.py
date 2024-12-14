#Write a python script to find the number of occurrences of a particular character present in the given string using a loop. (Don’t use string methods).

s=input("Enter a string")
c=input("Enter character to be searched")
count=0
for i in s:
    if(i==c):
       count=count+1
print(count)