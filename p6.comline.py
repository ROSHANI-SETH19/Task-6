import os
import random

# Define constants for game stats
MAX_HEALTH = 100
MAX_ATTACK = 20
MAX_DEFENSE = 10

# Define a Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.health = MAX_HEALTH
        self.attack = 10
        self.defense = 5
        self.inventory = []

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def deal_damage(self, enemy):
        damage = self.attack - enemy.defense
        if damage < 0:
            damage = 0
        enemy.take_damage(damage)

    def add_item(self, item):
        self.inventory.append(item)

    def equip_item(self, item):
        self.attack += item.attack
        self.defense += item.defense
        self.health += item.health
        self.inventory.remove(item)

# Define an Enemy class
class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def deal_damage(self, player):
        damage = self.attack - player.defense
        if damage < 0:
            damage = 0
        player.take_damage(damage)

# Define an Item class
class Item:
    def __init__(self, name, description, health=0, attack=0, defense=0):
        self.name = name
        self.description = description
        self.health = health
        self.attack = attack
        self.defense = defense

# Define a Game class
class Game:
    def __init__(self):
        self.player = Player("Hero")
        self.current_location = "town"
        self.locations = {
            "town": {
                "description": "You are in a bustling town.",
                "items": [Item("Sword", "A sharp sword.", attack=5)],
                "enemies": [Enemy("Goblin", 20, 5, 2)]
            },
            "forest": {
                "description": "You are in a dark forest.",
                "items": [Item("Shield", "A sturdy shield.", defense=3)],
                "enemies": [Enemy("Orc", 30, 10, 5)]
            }
        }

    def save_game(self):
        with open("savegame.txt", "w") as f:
            f.write(f"{self.player.name},{self.player.health},{self.player.attack},{self.player.defense},{self.current_location}\n")
            for item in self.player.inventory:
                f.write(f"{item.name},{item.description},{item.health},{item.attack},{item.defense}\n")

    def load_game(self):
        if os.path.exists("savegame.txt"):
            with open("savegame.txt", "r") as f:
                lines = f.readlines()
                player_data = lines[0].strip().split(",")
                self.player.name = player_data[0]
                self.player.health = int(player_data[1])
                self.player.attack = int(player_data[2])
                self.player.defense = int(player_data[3])
                self.current_location = player_data[4]
                self.player.inventory = []
                for line in lines[1:]:
                    item_data = line.strip().split(",")
                    item = Item(item_data[0], item_data[1], int(item_data[2]), int(item_data[3]), int(item_data[4]))
                    self.player.inventory.append(item)

    def play(self):
        print("Welcome to the game!")
        while True:
            print(f"\nYou are in {self.current_location}.")
            print(self.locations[self.current_location]["description"])
            print("What do you want to do?")
            print("1. Explore")
            print("2. Fight")
            print("3. Inventory")
            print("4. Save and quit")
            choice = input("> ")
            if choice == "1":
                self.explore()
            elif choice == "2":
                self.fight()
            elif choice == "3":
                self.show_inventory()
            elif choice == "4":
                self.save_game()
                print("Game saved!")
                break
            else:
                print("Invalid choice. Try again.")

    def explore(self):
        if self.current_location == "town":
            print("You see a forest to the north.")
            choice = input("Do you want to go to the forest? (yes/no) ")
            if choice.lower() == "yes":
                self.current_location = "forest"
        elif self.current_location == "forest":
            print("You see a town to the south.")
            choice = input("Do you want to go to the town? (yes/no) ")
            if choice.lower() == "yes":
                self.current_location = "town"

        # Pick up items in the current location
        items = self.locations[self.current_location]["items"]
        for item in items:
            print(f"You find a {item.name}: {item.description}")
            self.player.add_item(item)

    def fight(self):
        enemy = random.choice(self.locations[self.current_location]["enemies"])
        print(f"You encounter a {enemy.name}!")
        while self.player.is_alive() and enemy.is_alive():
            print(f"\n{self.player.name} vs {enemy.name}")
            print(f"{self.player.name}: Health={self.player.health}, Attack={self.player.attack}, Defense={self.player.defense}")
            print(f"{enemy.name}: Health={enemy.health}, Attack={enemy.attack}, Defense={enemy.defense}")
            
            # Player's turn
            self.player.deal_damage(enemy)
            print(f"{self.player.name} attacks {enemy.name}!")

            if not enemy.is_alive():
                print(f"{enemy.name} has been defeated!")
                break

            # Enemy's turn
            enemy.deal_damage(self.player)
            print(f"{enemy.name} attacks {self.player.name}!")

            if not self.player.is_alive():
                print(f"{self.player.name} has been defeated!")
                break

    def show_inventory(self):
        print(f"\n{self.player.name}'s Inventory:")
        if not self.player.inventory:
            print("Your inventory is empty.")
        else:
            for idx, item in enumerate(self.player.inventory, 1):
                print(f"{idx}. {item.name}: {item.description}")
            
            choice = input("Do you want to equip any item? (yes/no) ")
            if choice.lower() == "yes":
                try:
                    item_choice = int(input(f"Select an item (1-{len(self.player.inventory)}): ")) - 1
                    if 0 <= item_choice < len(self.player.inventory):
                        item = self.player.inventory[item_choice]
                        self.player.equip_item(item)
                        print(f"{self.player.name} equips {item.name}.")
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid choice.")

# Running the game
if __name__ == "__main__":
    game = Game()
    game.load_game()
    game.play()
