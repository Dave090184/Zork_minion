import tkinter as tk
from tkinter import messagebox
import random
import copy


# ==========================
# MAZE
# ==========================

maze = {

    "start": {
        "north": "hallway1",
        "east": "office",
        "story": "You are in the entrance hallway. A mysterious note warns you about danger ahead."
    },

    "hallway1": {
        "south": "start",
        "east": "library",
        "west": "kitchen",
        "story": "The hallway is dark. You hear strange Minion noises nearby."
    },

    "library": {
        "west": "hallway1",
        "north": "study",
        "story": "Smoke fills the library. A Banana Monster appears!"
    },

    "study": {
        "south": "library",
        "story": "An old study contains a hidden treasure chest."
    },

    "office": {
        "west": "start",
        "south": "kitchen",
        "story": "A computer is blinking on the desk."
    },

    "kitchen": {
        "north": "office",
        "story": "The kitchen is empty. You see banana footprints."
    }

}


# ==========================
# ENEMIES
# ==========================

enemy_template = {

    "library": {
        "name": "Banana Monster",
        "health": 50,
        "damage": 5
    },

    "study": {
        "name": "Grunt Minion",
        "health": 100,
        "damage": 10
    }

}


enemies = copy.deepcopy(enemy_template)



# ==========================
# PLAYER
# ==========================

player = {

    "health": 100,

    "inventory": [
        "sword",
        "shield"
    ]

}


location = "start"



# ==========================
# GAME FUNCTIONS
# ==========================

def update_screen(text):

    story_box.config(state="normal")
    story_box.delete("1.0", tk.END)

    story_box.insert(
        tk.END,
        text
    )

    story_box.config(state="disabled")


    stats.config(
        text=f"""
Location: {location}

Health: {player['health']}

Inventory:
{', '.join(player['inventory'])}
"""
    )



def move(direction):

    global location

    if direction in maze[location]:

        location = maze[location][direction]

        update_screen(
            maze[location]["story"]
        )

    else:

        update_screen(
            "You cannot go that way!"
        )



def attack():

    if location not in enemies:

        update_screen(
            "There is nothing to attack here."
        )

        return


    enemy = enemies[location]


    if enemy["health"] <= 0:

        update_screen(
            "This enemy is already defeated."
        )

        return



    damage = 20 if "sword" in player["inventory"] else 5

    enemy["health"] -= damage


    if enemy["health"] <= 0:

        update_screen(
            f"You defeated {enemy['name']}!"
        )


        if random.random() < 0.5:

            player["inventory"].append(
                "banana shield"
            )

            update_screen(
                f"You defeated {enemy['name']}!\n"
                "The enemy dropped a banana shield!"
            )


        return



    player["health"] -= enemy["damage"]


    if player["health"] <= 0:

        messagebox.showerror(
            "Game Over",
            "The Minions defeated you!"
        )

        root.destroy()

        return



    update_screen(
        f"""
You attacked {enemy['name']}!

Enemy health:
{enemy['health']}

The enemy hits you for:
{enemy['damage']}
"""
    )



def search():

    if location == "study":

        if "treasure key" not in player["inventory"]:

            player["inventory"].append(
                "treasure key"
            )

            update_screen(
                "You found a treasure key!"
            )

        else:

            update_screen(
                "The chest is empty."
            )



    elif location == "office":

        player["inventory"].append(
            "health potion"
        )

        update_screen(
            "You found a health potion!"
        )



    else:

        update_screen(
            "You found nothing."
        )



def use_item():

    if "health potion" in player["inventory"]:

        player["inventory"].remove(
            "health potion"
        )

        player["health"] += 30


        if player["health"] > 100:

            player["health"] = 100


        update_screen(
            "You drank the health potion!"
        )

    else:

        update_screen(
            "You don't have a usable item."
        )



# ==========================
# GUI
# ==========================

root = tk.Tk()

root.title(
    "Minion Maze"
)

root.geometry(
    "600x500"
)


title = tk.Label(
    root,
    text="MINION MAZE",
    font=("Arial", 20)
)

title.pack()



stats = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)

stats.pack()



story_box = tk.Text(
    root,
    height=10,
    width=60
)

story_box.pack()

story_box.config(
    state="disabled"
)



frame = tk.Frame(root)

frame.pack()



tk.Button(
    frame,
    text="North",
    width=10,
    command=lambda: move("north")
).grid(row=0,column=1)


tk.Button(
    frame,
    text="West",
    width=10,
    command=lambda: move("west")
).grid(row=1,column=0)


tk.Button(
    frame,
    text="East",
    width=10,
    command=lambda: move("east")
).grid(row=1,column=2)


tk.Button(
    frame,
    text="South",
    width=10,
    command=lambda: move("south")
).grid(row=2,column=1)



buttons = tk.Frame(root)

buttons.pack(pady=10)



tk.Button(
    buttons,
    text="Attack",
    width=12,
    command=attack
).grid(row=0,column=0)


tk.Button(
    buttons,
    text="Search",
    width=12,
    command=search
).grid(row=0,column=1)


tk.Button(
    buttons,
    text="Use Potion",
    width=12,
    command=use_item
).grid(row=0,column=2)



tk.Button(
    root,
    text="Exit",
    width=20,
    command=root.destroy
).pack()



update_screen(
    maze["start"]["story"]
)


root.mainloop()