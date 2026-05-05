import os
from data import player_inventory
from inventory import show_inventory, add_item, remove_item, update_quantity, find_item, filter_by_spec, total_inventory_price, get_all_categories
from utils import get_text, get_input


def main():
    last_output = ""

    while True:
        os.system("cls")
        
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

        if last_output:
            print(f"Last action output: \n\n{last_output}")

        try:    
            number = int(input("Choose option: "))

            if number == 0:
                print("Have a nice day")
                break
            
            elif number == 1:
                last_output = show_inventory(player_inventory)
            
            elif number == 2:
                print("Type the names/values of the corresponded things:\n")

                item = get_text("Item name: ", "Name cannot be a number")
                category = get_text("Category: ", "Category cannot be a number")
                price = get_input("Price: ", int, "Enter a valid number")
                quantity = get_input("Quantity: ", int, "Enter a valid number")
                rarity = get_text("Rarity: ", "Rarity cannot be a number")

                last_output = add_item(player_inventory, item.title(), category.lower(), price, quantity, rarity.lower())
            
            elif number == 3:
                item = get_text("Item name: ", "Name cannot be a number")

                last_output = remove_item(player_inventory, item.title())
            
            elif number == 4:
                item = get_text("Item name: ", "Name cannot be a number")
                quantity = get_input("Quantity: ", int, "Enter a valid number")

                last_output = update_quantity(player_inventory, item.title(), quantity)
            
            elif number == 5:
                item = get_text("Item name: ", "Name cannot be a number")

                last_output = find_item(player_inventory, item.title())
            
            elif number == 6:
                spec_name = get_text("Item spec: ", "Spec cannot be a number")
                target_value = input("Spec value: ").strip().lower()

                if target_value.isdigit():
                    target_value = int(target_value)

                last_output = filter_by_spec(player_inventory, spec_name.lower(), target_value)
            
            elif number == 7:
                last_output = f"Total inventory price = {total_inventory_price(player_inventory)}"

            elif number == 8:
                last_output = f"Categories: " + ", ".join(get_all_categories(player_inventory))

            else:
                last_output = "Choose a valid option from 0 to 8"


        except ValueError:
            last_output = "Menu option should be a number"

if __name__ == "__main__":
    main()