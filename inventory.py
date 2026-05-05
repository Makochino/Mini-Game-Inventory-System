from data import player_inventory

def show_inventory(inventory):
    result = []
    
    for item, specs in inventory.items():
        result.append(f"Item: {item}")
        result.append("Specs:")
        
        for spec, value in specs.items():
            result.append(f"   {spec}: {value}")

        result.append("")
    
    return "\n".join(result)


def add_item(inventory, item, category, price, quantity, rarity):
    if item in inventory:
        return f"{item} is already in your inventory"        
    
    if not isinstance(price, int) or price < 0:
        return "price should be int and non-negative"

    if not isinstance(quantity, int) or quantity < 0:
        return "Quantity should be int and non-negative"

    else:
        inventory[item] = {
            "category": category,
            "price": price,
            "quantity": quantity,
            "rarity": rarity
        }
        return f"Item {item} was added successfully to your inventory"

def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item)
        return f"Item {item} was removed successfully from your inventory"
    else:
        return f"Item {item} is not in your inventory"

def update_quantity(inventory, item, quantity):
    if item in inventory:
        before_change_quantity = inventory[item]["quantity"]
        
        if isinstance(quantity, int) and quantity >= 0:
            inventory[item]["quantity"] = quantity
            
            return f"{item} quantity was changed successfully from {before_change_quantity} to {quantity}"
        
        else:
            return f"{item} quantity should be 'int' and non-negative price"
    
    else:
        return f"{item} is not in your inventory"


def find_item(inventory, item):
    result = []
    
    if item in inventory:
        specs = inventory[item]
        
        result.append(f"Item: {item}")
        result.append("Specs:")


        for spec, value in specs.items():
            result.append(f"   {spec}: {value}")
        
        result.append("")
        
        return "\n".join(result)

    else:
        return f"Item {item} is not in your inventory"


def filter_by_spec(inventory, spec_name, target_value):
    result = []
    
    for item, specs in inventory.items():
    
        if spec_name in specs and specs[spec_name] == target_value:
            
            result.append(f"Item: {item}")
            result.append("Specs:")

            for spec, value in specs.items():
                result.append(f"   {spec}: {value}")
                    
            result.append("\n")
    
    if result: # or len(result) >= 1, we could write both ways, but first option more pythonic, because empty list == False
        return "\n".join(result) 
    else: 
        return f"No item found with {spec_name} = {target_value}" # переделать по гпт 


def total_inventory_price(inventory):
    total = 0

    for item, specs in inventory.items():
        total += specs["price"] * specs["quantity"]

    return total


def get_all_categories(inventory):
    categories = []

    for item, specs in inventory.items():
        if "category" in specs:
            categories.append(specs["category"])
    
    return set(categories)

print(filter_by_spec(player_inventory, "category", "weapon"))