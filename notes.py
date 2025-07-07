from characters import Character
from items import Item

# Create items
axe = Item("axe", "deal damage between 45 and 100")
beer = Item("beer", "restore 50 hp")
flashlight = Item("flashlight", "deal damage between 45 and 100")
potion = Item("potion", "restore 75 hp")
trap = Item("trap", "set a trap for enemies")
bow = Item("bow", "deal damage between 45 and 100")

# Create characters
jonathan = Character("Jonathan")
charles = Character("Charles")
guillaume = Character("Guillaume")
jack = Character("Jack")

# Give items
jonathan.add_item(axe)
charles.add_item(bow)

# Use items
jonathan.inventory[0].use(jonathan)
charles.inventory[0].use(charles)


