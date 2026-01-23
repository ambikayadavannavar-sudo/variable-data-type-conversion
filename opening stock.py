opening_stock = [100, 200, 150, 300]
closing_stock = [90, 220, 130, 310]
for i in range(len(opening_stock)):
    if closing_stock[i] > opening_stock[i]:
        print(f"Product {i+1}: Stock Increased")
    elif closing_stock[i] < opening_stock[i]:
        print(f"Product {i+1}: Stock Reduced")
    else:
        print(f"Product {i+1}: No Change")