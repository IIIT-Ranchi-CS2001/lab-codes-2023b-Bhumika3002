#Sort the list of tuples constructed above with and without sorted function. 
customer_names = [input("Enter customer name: ") for _ in range(3)]
customer_ids = [input("Enter customer ID: ") for _ in range(3)]
shopping_points = [int(input("Enter shopping points: ")) for _ in range(3)]

customers_with_zip = [(name, cid, points) for name, cid, points in zip(customer_names, customer_ids, shopping_points)]

print("List of tuples using zip():", customers_with_zip)
customers_without_zip = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]

print("List of tuples without using zip():", customers_without_zip)


sorted_customers = sorted(customers_with_zip, key=lambda x: x[2])

print("Sorted list of tuples using sorted():", sorted_customers)

for i in range(len(customers_without_zip)):
    for j in range(0, len(customers_without_zip) - i - 1):
        if customers_without_zip[j][2] > customers_without_zip[j + 1][2]:
            customers_without_zip[j], customers_without_zip[j + 1] = customers_without_zip[j + 1], customers_without_zip[j]

print("Sorted list of tuples without using sorted():", customers_without_zip)
