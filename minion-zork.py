import random

# Define the maze layout and story elements
maze = {
    "start": {
        "north": "hallway1",
        "east": "office",
        "story": "You find yourself in the hallway. A mysterious note is stuck to the wall, promising danger ahead.",
    },
    "hallway1": {
        "south": "start",
        "east": "library",
        "west": "kitchen",
        "story": "You enter the library. The air is thick with smoke, and the bookshelves are falling down. You need to find a way out before it collapses.",
    },
    "library": {
        "west": "hallway1",
        "north": "study",
        "story": "You find yourself in the library. A group of mischievous Minions are playing a game of marbles, but they seem to be losing.",
    },
    "study": {
        "south": "library",
    },
    "office": {
        "west": "start",
        "south": "kitchen",
        "story": "You find yourself in the office. A desk with a keyboard and a computer monitor sits in the center of the room.",
    },
    "kitchen": {
        "north": "office",
    },
}

# Define the player's inventory
inventory = {
    "sword": 1,
    "shield": 1,
}

# Define the enemies
enemies = {
    "grunt": {
        "name": "Grunt",
        "health": 100,
        "damage": 10,
    },
    "banana": {
        "name": "Banana",
        "health": 50,
        "damage": 5,
    },
}

# Initialize the player's location, health, and inventory
current_location = "start"
player_health = 100
player_inventory = []

# Print the welcome message
print("Welcome to the Minion Maze!")
print("You find yourself in the hallway.")

# Game loop
while True:
    # Print the player's location, health, and inventory
    print(f"You are in the {current_location}.")
    print(f"Health: {player_health}")
    print("Inventory:", player_inventory)

    # Get the player's input
    action = input("What do you want to do? ").lower()

    # Move north, south, east, or west
    if action in ["north", "south", "east", "west"]:
        current_location = maze[current_location][action]
        print(maze[current_location]["story"])
    
    # Check for enemies in the current location
    elif action == "attack":
        if current_location in enemies:
            enemy = enemies[current_location]
            print("A", enemy["name"], "appears!")

            # Battle loop
            while True:
                # Player attacks the enemy
                enemy["health"] -= player_inventory.get("sword", 0) * 10

                # Check if the enemy is dead
                if enemy["health"] <= 0:
                    print("You defeated the", enemy["name"] + "!")
                    break

                # Enemy attacks the player
                player_health -= enemy["damage"]

                # Check if the player is dead
                if player_health <= 0:
                    print("You died!")
                    break
    
    # Use an item from the inventory
    elif action.startswith("use"):
        item = input("Which item do you want to use? ")
        if item in player_inventory:
            print(f"You used {item}!")
        else:
            print(f"You don't have {item} in your inventory.")
    
    # Check for items in the current location
    elif action == "search":
        if maze[current_location].get("items", []):
            print("You found some items!")
            for item in maze[current_location]["items"]:
                inventory.append(item)
        else:
            print("There are no items here.")
    
    # Pick up an item from the ground
    elif action == "pickup":
        if current_location in enemies:
            enemy = enemies[current_location]
            if enemy["name"] in inventory:
                player_inventory.append(enemy["name"])
                print("You picked up", enemy["name"], "!")
            else:
                print("There is no item here.")
        else:
            print("There are no items here.")
    
    # Use a weapon from the inventory
    elif action.startswith("weapon"):
        weapon = input("Which weapon do you want to use? ")
        if weapon in player_inventory:
            print(f"You used {weapon}!")
        else:
            print(f"You don't have {weapon} in your inventory.")
    
    # Check for enemies in the current location
    elif action == "enemies":
        if current_location in enemies:
            enemy = enemies[current_location]
            print("A", enemy["name"], "appears!")
        else:
            print("There are no enemies here.")
    
    # Use a shield from the inventory
    elif action.startswith("shield"):
        if current_location in enemies:
            enemy = enemies[current_location]
            if enemy["name"] in player_inventory:
                player_inventory.append(enemy["name"])
                print("You used", enemy["name"], "!")
            else:
                print("There is no item here.")
        else:
            print("There are no items here.")
    
    # Check for a map in the current location
    elif action == "map":
        if maze[current_location].get("map", []):
            print(maze[current_location]["map"])
        else:
            print("There is no map here.")
    
    # Check for a treasure in the current location
    elif action == "treasure":
        if maze[current_location].get("treasure", []):
            print(maze[current_location]["treasure"])
        else:
            print("There is no treasure here.")
    
    # Exit the game
    elif action == "exit":
        break
    
    # Invalid input
    else:
        print("Invalid command. Type 'help' for a list of commands.")
