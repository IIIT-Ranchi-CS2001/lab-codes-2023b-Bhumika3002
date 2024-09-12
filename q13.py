#Write a python script to check whether all the characters present in a string are alphanumeric (uppercase letters, lowercase letters or digits) using for  with else. Print True if all characters are alphanumeric. Otherwise print False.
s=input("Enter a string")
for i in s:
    i.isupper()==1 or i.islower()==1 or i.isdigit()==1:
        print("True")
else:
    print("False") 