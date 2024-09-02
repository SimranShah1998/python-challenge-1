
# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        i += 1

    # Ask the customer to select a menu category by number
    menu_selection = input("Please select an item by number from the menu: ")

    # Check if the input is a number
    if not menu_selection.isdigit():
        print("Error: Please enter a valid number.")
        continue
    else:
        menu_selection = int(menu_selection)

    # Check if the menu selection is valid
    if menu_selection not in menu_items.keys():
        print("Error: Selected item is not available.")
        continue
    else:
        selected_category = menu_items[menu_selection]

    # Prompt for quantity of the selected item
    quantity = input(f"How many {selected_category} would you like? ")

    # Validate the quantity input
    if not quantity.isdigit():
        print("Invalid quantity. Defaulting to 1.")
        quantity = 1
    else:
        quantity = int(quantity)

    # Add the selected item, price, and quantity to the order list
    order.append({
        "Item name": selected_category,
        "Price": menu[selected_category],
        "Quantity": quantity
    })
while True:
    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o: ").strip().lower()
        if keep_ordering in ['y', 'yes']:
            break  # Continue the main loop to allow ordering another item
        elif keep_ordering in ['n', 'no']:
            place_order = False
            print("Thank you for your order.")
            break  # Break the loop to exit ordering
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        print("Thank you for your order.")
        break
    else:
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")



# Print the order receipt
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

for item in order:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]

    # Calculate spacing
    spaces_name = " " * (26 - len(item_name))
    spaces_price = " " * (7 - len(f"${price:.2f}"))

    # Print receipt line
    print(f"{item_name}{spaces_name}| ${price:.2f}{spaces_price}| {quantity}")

# Calculate and display the total price of the order
total_price = sum([item["Price"] * item["Quantity"] for item in order])
print(f"\nTotal Price: ${total_price:.2f}")
