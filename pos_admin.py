from handy_functions import read_json, load_json
from receipts import Receipts
from edit_goods import EditGoods

class POSAdmin:
    """runs admin application"""

    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.receipts = Receipts()
        self.edit = EditGoods(self.file_name)

    def display_items(self):
        """Shows a list of items/prices in inventory"""
        inventory = read_json(self.file_name)
        for d in inventory:
                print(f"{d['name']}: {d['price']}")

    def display_receipts(self):
        """Displays compiled receipt information"""
        gross = self.receipts.total_income()
        tax_owed = self.receipts.total_tax_owed()
        return {"Gross Income": gross, "Total Tax Owed": tax_owed}

    def edit_goods(self):
        """Allows admin to add/edit/delete items"""
        item = None
        show = None
        action = input("would you like to create or edit your inventory?('create'/'edit'): ")
        if action[0].lower() == 'c':
                self.edit.create_inventory()
        while True:
            if action[0].lower() == 'e':
                caption = "Would you like to: \n"
                caption += "add an item('add')\n"
                caption += "delete and item('del')\nor\n"
                caption += "edit an item('edit')\n: "
                edit = input(caption)
                if edit[0].lower() == 'a':
                    self.edit.add_item()
                elif edit[0].lower() == 'd':
                    item = input("Delete which item?: ")
                    self.edit.delete_item(item)
                elif edit[0].lower() == 'e':
                    item = input("Edit which item?: ")
                    self.edit.edit_item(item)
                else:
                    show = input("Would you like to see the inventory?(y/n): ")
                    if show[0].lower() == 'y':
                        self.display_items()
            again = input('Do you have more edits to make?(y/n): ')
            if again[0].lower() == 'n':
                break

    def admin(self):
        """allows admin access to POS system: 
        receipts reports/deletion, inventory creation/edits[item additions/deletions/edits]"""
        totals = {}
        store = None
        date = None
        save = {}
        sure = None
        print("Hello Admin,\nWelcome!")
        while True:
            action = input("What would you like to work on today?(receipts/inventory/): ")
            #*
            if action is None or len(action) == 0:
                print("You must enter an action!")
                continue
            if action[0].lower() == 'r':
                #*
                r_action = ""
                while len(r_action) < 1:
                    r_action = input("Receipt totals or delete receipts?(totals/delete): ")
                    if r_action is None or len(r_action) == 0:
                        print("Please enter totals or delete!")
                if r_action[0].lower() == 't':
                    totals = self.display_receipts()
                    print(totals)
                    store = input("Store totals?(y/n): ")
                    date = input("Today's date?: ")
                    save = {date: totals}
                    if store[0].lower() == 'y':
                        load_json("receipt_totals.json", save)
                elif r_action[0].lower() == 'd':
                    sure = input("Are you sure you want to delete the current receipts file?(y/n): ")
                    if sure[0].lower() == 'y':
                        self.receipts.delete_receipts()
            if action[0].lower() == 'i':
                i_action = input("Show or edit inventory?(show/edit): ")
                if i_action[0].lower() == 's':
                    self.display_items()
                elif i_action[0].lower() == 'e':
                    self.edit_goods()
            again = input('Do you have more to do?(y/n): ')
            if again[0].lower() == 'n':
                break

def main():
    """test"""
    # admin = POSAdmin('gardens_shop.json')
    # admin.display_items()
    # print(admin.display_receipts())
    # admin = POSAdmin('sports_shop.json')
    # admin.edit_goods()
    admin = POSAdmin('ice_cream_shop.json')
    admin.admin()

if __name__ == "__main__":
    main()
