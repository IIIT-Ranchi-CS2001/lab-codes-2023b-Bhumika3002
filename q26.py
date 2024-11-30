#Define a function my_zip() that can form a list of tuples by iterating the following customer details:- ‘customer Name, customer ID , shopping points’ and based on the keyword parameter ‘strct’: If strct = True, zipping shall be done only if all lists are of equal length. If strct = False, zipping can be done by taking the minimum length of the iterable.
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
