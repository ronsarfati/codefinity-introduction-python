# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for items, details in products.items():
    details[0] = float(details[0])
    details[1] = int(details[1])
    current_sales = details[0] * details[1]
    total_sales_list.append(current_sales)
    #print(total_sales_list)
    total_sales = float(total_sales_list[0])
    print(f"Total sales for {items}: ${current_sales}")

    total_sum = sum(total_sales_list)
print(" ")
print(f"Total sum of all sales:${total_sum}")
    
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

print(" ")

print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")

    