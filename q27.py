'''Define a function my_sort() to sort the list of tuples created using my_zip function in the last question. The function must have two types of arguments- the list that carry the data, the key that determines the argument of sorting:
[Usage of built-in function sorted() is a punishable offense]
Key = 0: sorting based on customer name in ascending order
Key = 1: sorting based on Customer ID
Key = 2: sorting based on shopping points'''
def my_zip(list1, list2, list3, strct=True):
    if strct:
        if len(list1) == len(list2) == len(list3):
            return [(list1[i], list2[i], list3[i]) for i in range(len(list1))]
        else:
            raise ValueError("All lists must be of equal length in strict mode.")
    else:
        min_length = min(len(list1), len(list2), len(list3))
        return [(list1[i], list2[i], list3[i]) for i in range(min_length)]


customer_names = ['Alice', 'Bob', 'Charlie']
customer_ids = ['C001', 'C002']
shopping_points = [150, 200, 300]

try:
    strict_zip = my_zip(customer_names, customer_ids, shopping_points, strct=True)
    print("Strict zip:", strict_zip)
except ValueError as e:
    print("Error:", e)

non_strict_zip = my_zip(customer_names, customer_ids, shopping_points, strct=False)
print("Non-strict zip:", non_strict_zip)

def my_sort(data, key=0):

    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


customer_names = ['Alice', 'Bob', 'harlie']
customer_ids = ['C001', 'C002', 'C003']
shopping_points = [150, 200, 300]

customers = my_zip(customer_names, customer_ids, shopping_points, strct=False)

sorted_by_name = my_sort(customers[:], key=0)  
print("Sorted by name:", sorted_by_name)

sorted_by_id = my_sort(customers[:], key=1)
print("Sorted by ID:", sorted_by_id)

sorted_by_points = my_sort(customers[:], key=2)
print("Sorted by shopping points:", sorted_by_points)

