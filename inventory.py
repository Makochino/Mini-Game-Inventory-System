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


def show_inventory(player_inventory):
    for item, specs in player_inv.items():
        print(f"Item: {item}\nSpecs:")
        for spec, value in specs.items():
            print(f"   {spec}: {value}")
        print()


def add_item(player_inv):
    

show_inventory(player_inventory)
