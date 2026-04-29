def apply_discount(price, discount = 0.05):
    price_after_dicsount = price - price * discount
    return price_after_dicsount

def apply_tax(price, tax = 0.07):
    price_after_tax = price + price * tax
    return price_after_tax

def calculate_total(price, discount = 0.05, tax = 0.07):
    total_price = apply_tax(apply_discount(price, discount), tax)
    return total_price

total_price_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_price_default}")

total_price_custom = calculate_total(100, discount =  0.10, tax = 0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")
    

 