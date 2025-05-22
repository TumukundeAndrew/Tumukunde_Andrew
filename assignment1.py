# List of stock items (each item is a list: [name, quantity])
inventory = [
    ["Pineapples", 10],
    ["Tomatoes", 20],
    ["O1ranges", 15]
]

# display all products avilable in the inventory
def display_inventory():
    print("\nCurrent Inventory:")
    print("------------------")
    for item in inventory:
        print(f"{item[0]} - Quantity: {item[1]}")
    print("------------------")
    
# update any product from the inventory by changing the quanttity
def update_inventory():
    item_name = input("Enter item name to update: ").capitalize()
    found = False
    for item in inventory:
        if item[0] == item_name:
            new_quantity = int(input(f"Enter new quantity for {item_name}: "))
            item[1] = new_quantity
            print(f"{item_name} updated to quantity {new_quantity}.")
            found = True
            break
    if not found:
        print(f"{item_name} not found in inventory.")

# add another product to the inventory
def add_item():
    item_name = input("Enter new item name: ").capitalize()
    quantity = int(input(f"Enter quantity for {item_name}: "))
    inventory.append([item_name, quantity])
    print(f"{item_name} added with quantity {quantity}.")

def main():
    while True:
        display_inventory()
        print("Options:")
        print("1. Update Item")
        print("2. Add New Item")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            update_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
