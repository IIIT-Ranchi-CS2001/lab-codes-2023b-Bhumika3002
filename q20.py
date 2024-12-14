#Generate three lists using list comprehension. List of names, list of Roll nos and list of marks for Physics exam for all students of the class. Create a list of tuples using the zip function where each tuple carries individual student details. Sort the list of tuples using a sorted function by keeping Marks as the key for sorting.
names=["Shinchan","Salman Khan","Radhe Bhaiya","Lalu Yadav"]
roll=[2,3,1,4]
marks=[45,93,73,60]
student=list(zip(names,roll,marks))
sorted_students=sorted(student , key=lambda student:student[2])
print(sorted_students)