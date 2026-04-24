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


def add_item(inventory, name, category, value, quantity, rarity):
    if name not in inventory:
        inventory.update({
            name: {
                "category": category,
                "value": value,
                "quantity": quantity,
                "rarity": rarity}
        })
        return "Item added successfully"
    else:
        return "Error this item already exists try again"


print(add_item(player_inventory, "Legendary Bow", "weapon", 450, 1, "Legendary⭐"))
print(show_inventory(player_inventory))
