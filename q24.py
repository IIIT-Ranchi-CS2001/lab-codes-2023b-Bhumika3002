#Enter three lists using list comprehension: Customer name, Customer ID, and shopping points. Construct a list of tuples with and without using built-in function zip().
customer_names = [input("Enter customer name: ") for _ in range(3)]
customer_ids = [input("Enter customer ID: ") for _ in range(3)]
shopping_points = [int(input("Enter shopping points: ")) for _ in range(3)]

customers_with_zip = [(name, cid, points) for name, cid, points in zip(customer_names, customer_ids, shopping_points)]

print("List of tuples using zip():", customers_with_zip)
customers_without_zip = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]

print("List of tuples without using zip():", customers_without_zip)
