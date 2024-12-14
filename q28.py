'''Write program to define a function my_max() to complete the following tasks: [Usage of built-in function max() is strictly prohibited]
If a list of integers is passed as the input argument, the function shall return maximum value present in the list
If a set is passed, maximum value present in the list
If a tuple is passed, maximum value present in the tuple
Hint: Pass the container type unpacked using *'''
def my_max(*args):
   
    if len(args) == 0:
        raise ValueError("my_max() requires at least one element")
    
    maximum = args[0]
    
    for value in args:
        if value > maximum:
            maximum = value
    
    return maximum


numbers_list = [10, 20, 30, 40, 50]
print("Maximum in list:", my_max(*numbers_list))

numbers_set = {5, 15, 25, 35, 45}
print("Maximum in set:", my_max(*numbers_set))

numbers_tuple = (7, 14, 21, 28, 35)
print("Maximum in tuple:", my_max(*numbers_tuple))

