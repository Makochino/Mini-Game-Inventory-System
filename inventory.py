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
        if item != None:
            result.append(f"Item: {item}")
            result.append("Specs:")
            
            for spec, value in specs.items():
                result.append(f"   {spec}: {value}")

            result.append("")
        else:
            result.append("")
    return "\n".join(result)


def add_item(inventory, name, category, value, quantity, rarity):
    inventory.update({
        name: {
            "category": category,
            "value": value,
            "quantity": quantity,
            "rarity": rarity}
    })
    return f"Item {name} added successfully"

def remove_item(player_inventory, item):
    if item in player_inventory:
        player_inventory.pop(item)
        return f"Item {item} removed successfully"
    else:
        return f"Item {item} doesn't contain in your inventory!!!"

print(add_item(player_inventory, "Legendary Bow", "weapon", 450, 1, "Legendary⭐"))
print(remove_item(player_inventory, "Iron Sword"))
print(show_inventory(player_inventory))