'''Define a function Create_Array () that can create an array of flexible size according to the number of arguments passed within the function call. The elements passed in the function should make the diagonal Elements of the array and the rest of the elements can be all zeros
For Example, if the function call is Create_Array(1,2,3,4)
The function shall return
1 0 0 0
0 2 0 0
0 0 3 0
0 0 0 4

'''
import numpy as np

def Create_Array(*args):
    n = len(args)
    
    matrix = np.zeros((n, n), dtype=int)
    
    for i in range(n):
        matrix[i, i] = args[i]
    
    return matrix

result = Create_Array(1, 2, 3, 4)
print(result)
