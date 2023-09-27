import os
from handy_functions import read_json, load_json
ROOT_DIR = os.path.dirname(__file__)

class EditGoods:
    """enables admin to create/add/edit/delete items from the inventory"""

    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.file_path = os.path.join(ROOT_DIR, self.file_name)
        self.inventory = []        

    def create_inventory(self):
        """creates inventory"""
        print("Type 'q' to exit.")
        while True:
            name = input("What would you like to add?: ")
            if name[0].lower() == 'q':
                break
            price = input("How much will this cost?: ")
            item = {'name': name, 'price': price}
            self.inventory.append(item)
        load_json(self.file_name, self.inventory)

    def add_item(self):
        """adds item to inventory"""
        self.inventory = read_json(self.file_name)
        name = input("What would you like to add?: ")
        price = input("How much will this cost?: ")
        item = {'name': name, 'price': price}
        self.inventory.append(item)
        load_json(self.file_name, self.inventory)

    def delete_item(self, item):
        """deletes an item from inventory"""
        target_dict = None
        self.inventory = read_json(self.file_name)
        for d in self.inventory:
            if d['name'] == item:
                target_dict = d
        if target_dict == None:
            print('This item does not exist.')
        else:
            self.inventory.remove(target_dict)
            load_json(self.file_name, self.inventory)

    def edit_item(self, item):
        """edits an item in the inventory"""
        target_dict = None
        new_name = None
        new_price = None
        self.inventory = read_json(self.file_name)
        for d in self.inventory:
            if d['name'] == item:
                target_dict =d
        if target_dict == None:
            print('This item does not exist.')
        else:
            print(target_dict)
            name_or_price = input("Would you like to change the [name] or the [price]?: ")
            if name_or_price[0].lower() == 'n':
                new_name = input("What is the item's new name?: ")
                target_dict['name'] = new_name
            elif name_or_price[0].lower() == 'p':
                new_price = input("What is the item's new price?: ")
                target_dict['price'] = new_price
            else:
                print("You must pick 'name' or 'price'.")
            load_json(self.file_name, self.inventory)

def main():
    """test"""
    admin = EditGoods("gardens_shop.json")
    # admin.create_inventory()
    # admin.add_item()
    # admin.delete_item('q')
    # admin.edit_item('mulch')
    

if __name__ == "__main__":
    main()
