'''Write a python script using map, lambda and filter functions to do the following operations on a user inputted comma separated strings: E.g.: “Tom 25 Rahu22 2@$” 
To find all the letters given in the string and to convert them to uppercase
o/p: [‘TOM’]
To find all the digits present in the string and to find their squares
o/p: [625]
To display all the alphanumeric characters present in the string
o/p: [“Tom”, ‘25’, “Rahu22”]'''
input_string = input("Enter a comma-separated string: ")

input_list = input_string.split(',')

letters_uppercase = list(
    map(lambda s: s.upper(), filter(lambda s: s.isalpha(), input_list))
)
print("Uppercase letters:", letters_uppercase)

digits_squared = list(
    map(lambda s: int(s) ** 2, filter(lambda s: s.isdigit(), input_list))
)
print("Squares of digits:", digits_squared)

alphanumeric = list(
    filter(lambda s: s.isalnum(), input_list)
)
print("Alphanumeric characters:", alphanumeric)

