"""
Task 1:
You are managing the product catalogs for an online store. Each catalog is a tuple of products, and each product is a tuple containing the product name and price. Merge multiple catalogs into a single tuple.
    - Write a function to join two or more product catalogs into one.
    - Display the combined catalog, ensuring that it maintains the order of products as they were in their original catalogs.
"""


def join_catalogs(catalog_1, catalog_2):
    combined_catalog = catalog_1 + catalog_2
    return combined_catalog


catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

if __name__ == "__main__":
    print(join_catalogs(catalog1, catalog2))
