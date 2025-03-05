# -add_to_checkout
# -display_goods (would add item to check-out)
# -item_lookup (would add item to check-out)(based on name or number)
import os
from handy_functions import read_json, load_json
ROOT_DIR = os.path.dirname(__file__)

class Goods:
    """allows access to inventory for selection"""

    def __init__(self, file_name) -> None:
        """
        Initializer for Goods class.
        Sets file path and name from argument given.
        Initializes empty checkout_list.
        """
        self.checkout_list = []
        self.file_name = file_name
        self.file_path = os.path.join(ROOT_DIR, self.file_name)

    def add(self, item):
        """adds an item to the checkout list"""
        self.checkout_list.append(item)

    def display_goods(self):
        """displays inventory list to pick from and add to order."""
        inventory = read_json(self.file_name)
        while True:
            target_d = None
            for d in inventory:
                print(f"{d['name']}: {d['price']}")
            add_to_order = input("(Type 'q' to quit.)\nWhat item would you like to add to your order?: ")
            if add_to_order[0].lower() == 'q':
                break
            for d in inventory:
                if d['name'] == add_to_order:
                    target_d = d
            if target_d == None:
                print("Sorry! We don't carry that item.(check spelling)")
                continue
            if target_d != None:
                self.add(target_d)

            

    def item_lookup(self):
        """
        allows user to look up an item typing in it's name, 
        asks to show inventory list if the item searched for is not in inventory,
        adds item to order once found
        """
        inventory = read_json(self.file_name)
        print('Type "q" to quit.')
        while True:
            lookup = None
            order = None
            target_d = None
            display = None
            lookup = input('What item would you like to look for?: ')
            if lookup == '':
                continue
            elif lookup[0].lower() == 'q':
                break
            for d in inventory:
                if d['name'] == lookup:
                    target_d = d
            if target_d == None:
                print("Sorry! We don't carry that item.(check spelling)")
                display = input("Would you like to see a list of our wares?")
                if display[0].lower() == 'y':
                    for d in inventory:
                        print(f"{d['name']}: {d['price']}")
                else:
                    continue
            if target_d != None:
                print(f"{target_d['name'].title()}, ${target_d['price']}")
                # order = input("Add item to order?(yes/no): ")
                # if order[0].lower() == 'y':
                self.add(target_d)
                continue
                # else: 
                #     continue

                #not sure if above commented-out section is useful or cumbersome...
    
    def make_order(self):
        load_json('order.json', self.checkout_list)

def main():
    """test"""
    goods = Goods('gardens_shop.json')
    # goods.add("gnome")
    # goods.display_goods()
    goods.item_lookup()
    print(goods.checkout_list)
    goods.make_order()
    



if __name__ == "__main__":
    main()