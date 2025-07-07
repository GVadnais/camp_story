class characters:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up a {item.name}")

    def show_inventory(self):
        print(f"{self.name}'s Inventory:")
        for item in self.inventory:
            print(f"- {item.name}")

    def equip_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.equipped_item = item
                item.is_equipped = True
                print(f"{self.name} equipped {item.name}")
                return
        print(f"{self.name} doesn’t have {item_name} in their inventory!")

    def get_damage(self, amount):
        self.hp -= amount
        self.hp = max(0, self.hp)  # Don't go below 0
        print(f"{self.name} takes {amount} damage! HP is now {self.hp}")

    def get_heal(self, amount):
        self.hp += amount
        self.hp = min(100, self.hp)  # Don't go above 100
        print(f"{self.name} heals {amount} HP! HP is now {self.hp}")