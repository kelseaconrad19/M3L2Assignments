"""
Task 1:
    - Write a function to iterate over the list of orders.
    - Unpack each tuple in the list and format the details for display.
"""


def display_orders(list_of_orders):
    for order in list_of_orders:
        customer_name, item, quantity = order
        print(f"Name: {customer_name}\n Item Ordered: {item}\n Quantity: {quantity}\n")


orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]

if __name__ == "__main__":
    display_orders(orders)

""" 
Task 2:
    - You have a list of contacts, where each contact is represented as a tuple containing a name, email, and phone number. Your task is to:
        - Sort the contacts by name.
        - Filter and display contacts whose names start with a specific letter.
"""


def sort_by_name(contact_list):
    return sorted(contact_list)


def filter_by_letter(contact_list):
    filter_list = []
    letter_filter = input("Enter a letter: ").upper()
    for c in contact_list:
        contact_name, contact_email, phone_number = c
        if contact_name.startswith(letter_filter):
            filter_list.append(c)
    return filter_list


contacts = [
    ("Walter", "alice@email.com", "123-456-7890"),
    ("Jesse", "bob@email.com", "234-567-8901"),
    ('Tim', "tim@email.com", "243-495-9879"),
    ('Marnie', "marnie@email.com", "456-018-6798"),
    ('Jimmy', "jimmy@email.com", "563-123-4562"),
    ('Jane', "jane@email.com", "983-897-1238"),
]

if __name__ == "__main__":
    print(sort_by_name(contacts))
    print(filter_by_letter(contacts))
