#Find the number of palindrome words in the given sentence without using any function.
s=input("Enter sentence")
l=s.split()
count=0
for i in l:
    if(i==i[::-1]):
        count=count+1
print(count)