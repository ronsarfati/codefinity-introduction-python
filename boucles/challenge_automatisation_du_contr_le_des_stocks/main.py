# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")
for article , details in inventory.items():
    current_stock = details[0]
    minimum_stock = details[1]
    restock_quantity = details[2]
    statut_of_sale = details [3]
    print(f"Processing {article}")

    while current_stock < minimum_stock:
        current_stock+= restock_quantity
        
        inventory[article][0]= current_stock
        
        if current_stock > discount_threshold and statut_of_sale == False: 
            inventory[article][3] = True
print("Processing completed ")
            
    