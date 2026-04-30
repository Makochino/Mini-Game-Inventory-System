player_inventory = {
    "Iron Sword": {
        "category": "weapon",
        "value": 120,
        "quantity": 1,
        "rarity": "common",
    },
    "Health Potion": {
        "category": "potion",
        "value": 30,
        "quantity": 5,
        "rarity": "uncommon",
    },
}


def show_inventory(inventory):
    result = []
    
    for item, specs in inventory.items():
        result.append(f"Item: {item}")
        result.append("Specs:")
        
        for spec, value in specs.items():
            result.append(f"   {spec}: {value}")

        result.append("")
    
    return "\n".join(result)


def add_item(inventory, item, category, value, quantity, rarity):
    if item in inventory:
        return f"{item} is already in your inventory"        
    
    if not isinstance(value, int) or value < 0:
        return "Value should be int and non-negative"

    if not isinstance(quantity, int) or quantity < 0:
        return "Quantity should be int and non-negative"

    else:
        inventory[item] = {
            "category": category,
            "value": value,
            "quantity": quantity,
            "rarity": rarity
        }
        return f"Item {item} was added successfully to your inventory"

def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item)
        return f"Item {item} was removed successfully from your inventory\n"
    else:
        return f"Item {item} is not in your inventory!!!\n"

def update_quantity(inventory, item, quantity):
    if item in inventory:
        if isinstance(quantity, int) and quantity >= 0:
            inventory[item]["quantity"] = quantity
            return f"{item} quantity was changed successfully)\n"
        else:
            return f"{item} quantity should be 'int' and non-negative value\n"
    else:
        return f"{item} is not in your inventory!!\n!"


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


def filter_by_category(inventory, category):
    result = []
    
    for item, specs in inventory.items():
        
        if specs["category"] == category:
            specs = inventory[item]
            result.append(f"Item: {item}")
            result.append("Specs:")

            for spec, value in specs.items():
                result.append(f"   {spec}: {value}")
                    
            result.append("")
   
    
    if result: # or len(result) >= 1, we could write both ways, but first option more pythonic, because empty list == False
        return "\n".join(result) 
    else: 
        return f"Item of such category({category}) is not in your inventory"


print(add_item(player_inventory, "Legendary Bow", "weapon", 450, 1, "⭐ Legendary ⭐"))
print(remove_item(player_inventory, "Iron Sword"))
print(update_quantity(player_inventory, "Legendary Bow", 2))
print(filter_by_category(player_inventory, "weapon"))