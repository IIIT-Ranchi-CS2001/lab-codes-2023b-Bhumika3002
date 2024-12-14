#Create a list of int using list comprehension [multiple input from keyboard].  Find the mean, median, and mode of the given list.
l=[1,2,3,5,2,8,4,0,74]
sum=0
n=len(l)
for i in l:
    sum=sum+i
    mean=sum/n
l.sort()
if n % 2 == 0:
       median= (l[n//2 - 1] + l[n//2]) / 2
else:  
       median = l[n//2]
f = {}
for i in l:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1



max= 0
for key, value in f.items():
    if value > max:
        max = value
        mode = key

print("Mean=",mean)
print("Median=",median)
print("Mode=",mode)