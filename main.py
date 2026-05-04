from data import player_inventory
from inventory import *
from utils import *

while True:
    try:
        print("""
===== Inventory Menu =====
    1. Show inventory
    2. Add item
    3. Remove item
    4. Update quantity
    5. Find item
    6. Filter search by spec
    7. Show total price
    8. Show all categories
    0. Exit
    """)
        number = int(input("Choose option: "))
        
        if number == 0:
            print("Have a nice day")
            break
        
        elif number == 1:
            print(show_inventory(player_inventory))
        
        elif number == 2:
            print("Type the names/vales of the corresponded things:\n")

            item = get_text("Item name: ", "Name cannot be a number")
            category = get_text("Category: ", "Category cannot be a number")
            price = get_input("Price: ", int, "Enter a valid number")
            quantity = get_input("Quantity: ", int, "Enter a valid number")
            rarity = get_text("Rarity: ", "Rarity cannot be a number")

            print(add_item(player_inventory, item, category, price, quantity, rarity))
            
    except ValueError:
        print("The input should be of the requested value")