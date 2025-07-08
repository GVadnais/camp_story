from characters import characters
from items import Item

def main():
    """
    This is the main function where the program's primary logic resides.
    """
    print("This code runs when the script is executed directly.")\
    
    
    beer = Item('beer', 'gives hp')

    character_name = input('Please choose your character name ')
    character_name = characters(character_name)
    
    print(f"once supon a time, a dude named {character_name}")



    character_name.add_item(beer)
    character_name.get_damage(50)
    beer.use(character_name)

if __name__ == "__main__":
    main()

