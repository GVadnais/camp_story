from characters import characters
from items import Item

def main():
    """
    This is the main function where the program's primary logic resides.
    """
    print("This code runs when the script is executed directly.")\
    
    jonathan = characters('Jonathan')
    beer = Item('beer', 'gives hp')
    jonathan.add_item(beer)

if __name__ == "__main__":
    main()

