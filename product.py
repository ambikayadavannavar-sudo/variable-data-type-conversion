products = {
    "Laptop": "Electronics",
    "Chair": "Furniture",
    "Mobile": "Electronics"
}
print("Product Names:")
for product in products.keys():
    print(product)
print("\nCategories:")
for category in products.values():
    print(category)
print("\nTotal Products:", len(products))