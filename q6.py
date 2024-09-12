#Write a python script to enter any string at run time and check whether it is a palindrome or not.
S=input("Enter a string")
if(S==S[::-1]):
    print("Palindrome")
else:
    print("Not a palindrome")

