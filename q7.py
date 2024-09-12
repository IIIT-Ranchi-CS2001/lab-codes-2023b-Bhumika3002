#Enter the following details of a student at run time: - Name, Roll number and marks secured for Mathematics Examination out of 100. Write a python script to display student details as shown:
#Name:
#Roll Number:
#Marks:
#Grade Point:
#Remark:
name=input("Enter name of student")
roll=int(input("Enter roll no. of student"))
marks=int(input("Enter marks of student in maths"))
if marks>=90:
    grade=10
    remark="OUTSTANDING"
elif marks>=80 and marks<90:
    grade=9
    remark="VERY GOOD"
elif marks>=70 and marks<80:
    grade=8
    remark="GOOD"
elif marks>=60 and marks<70:
    grade=7
    remark="AVERAGE"
elif marks>=50 and marks<60:
    grade=6
    remark="PASS"
else:
    grade=0
    remark="FAIL"
print("Name:",name)
print("Roll Number:",roll)
print("Marks:",marks)
print("Grade Point:",grade)
print("Remark:",remark)    
                 
        