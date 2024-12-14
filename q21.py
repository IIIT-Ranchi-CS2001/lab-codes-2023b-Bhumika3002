#Redo question 2 without using zip and sorted functions.

names = ["Shinchan", "Salman Khan", "Radhe Bhaiya", "Lalu Yadav"]
roll = [2, 3, 1, 4]
marks = [45, 93, 73, 60]


n = len(marks)
for i in range(n):
    for j in range(0, n-i-1):
        if marks[j] > marks[j+1]:
            
            marks[j], marks[j+1] = marks[j+1], marks[j]
           
            names[j], names[j+1] = names[j+1], names[j]
            
            roll[j], roll[j+1] = roll[j+1], roll[j]

for i in range(n):
    print(f"Name: {names[i]}, Roll: {roll[i]}, Marks: {marks[i]}")
