prices = [29.99, 45.50, 12.75, 38.20]
promotion = [0.10, 0.20, 0.15, 0.05]
updated_prices = []

for index in range(len(prices)):
    prices[index] -= prices [index] * promotion[index]
    updated_prices.append(prices[index])
    print(f"Updated price for item {index}: {prices[index]:.2f}$")