# collection_game v0.1
# Create a list variable named playerInventory.
# Use a while loop to allow the user to enter 10 items into the player inventory. 
# Sort the inventory.
# Display all items in the player inventory.

player_inventory = []
item_chosen = ""
items_chosen = -1
items_left = 10

while player_inventory != 10:
    print(f"You have {items_left - items_chosen} inventory space left.\n")
    item_chosen = input("What items would you like to add?")
    print(f"You have chosen {item_chosen} to go into your inventory\n")
    player_inventory.append(item_chosen)
    print(player_inventory)
    
    
    #player_inventory.sort()
print(f"You have {player_inventory} in iventory.")