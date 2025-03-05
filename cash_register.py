import os
from goods import Goods
from calculator import Calculator
from handy_functions import read_json, load_json
ROOT_DIR = os.path.dirname(__file__)

class CashRegister:
    """
    Point of sale
    shop inventory file: file_name must be added as an argument
    """

    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.file_path = os.path.join(ROOT_DIR, self.file_name)
        self.goods = Goods(file_name)
        self.calc = Calculator()
        self.subtotal = 0
        self.tax = 0
        self.total = 0
        self.order_number = 1
        # creates/reads order number file
        # with open('order_number.txt', 'r') as f:
        #     self.order_number = int(f.read())

    def scan_in(self):
        """add items to order"""
        method = "invalid"
        while method[0].lower() != 'n' and method[0].lower() != 'l':
            method = input('Search by [name] or [list]?: ')
            if method[0].lower() == 'n':
                self.goods.item_lookup()
                self.goods.make_order()
            elif method[0].lower() == 'l':
                self.goods.display_goods()
                self.goods.make_order()
            else:
                print('Invalid input. Please try again.')

    def pay(self):
        """
        calculates prices and tax totaled and returned
        creates receipt
        """
        paid = False
        self.total = self.calc.calc_total()
        self.subtotal = self.calc.subtotal
        self.tax = self.calc.tax
        print(f'Your total is: {self.total}')
        pay = input("Did the customer pay?: [y|n]")
        if pay[0].lower() == 'y':
            paid = True
        if paid == True:
            self.receipt()
            self.reset_order()
        # maybe unnecessary to keep track of cancelled orders...
        elif paid == False:
            print('Order cancelled')
            order = read_json('order.json')
            cancelled = read_json('cancelled_orders.json')
            cancelled.append(order)
            load_json('cancelled_orders.json', cancelled)
            self.reset_order()

    def receipt(self):
        """
        creates and stores individual receipt dictionaries in the receipt.json file
        """
        receipts = read_json('receipts.json')
        order = read_json('order.json')
        receipt = {}
        receipt['order #'] = self.order_number
        receipt['subtotal'] = self.subtotal
        receipt['tax'] = self.tax
        receipt['total'] = self.total
        receipt['items'] = order
        receipts.append(receipt)
        load_json('receipts.json', receipts)

    def reset_pay_totals(self):
        """resets totals between transactions"""
        self.subtotal = 0
        self.tax = 0
        self.total = 0

    def reset_order(self):
        """resets the order.json file between transactions"""
        order = os.path.join(ROOT_DIR, 'order.json')
        os.remove(order)
        load_json('order.json', [])
        self.goods.checkout_list = []

    def shop(self):
        """
        POS system executes 
        asks cashier if ready to checkout
        if ready, resets totals and scans in items/handles payment/creates receipt/increments order number
        if not ready, exits
        """
        while True:
            run = input("Hello cashier! Ready to checkout?[y|n]: ")
            if run[0].lower() == 'n':
                break
            if run[0].lower() == 'y':
                self.reset_pay_totals()
                self.scan_in()
                self.pay()
                self.order_number += 1
                # records/updates order number
                # with open('order_number.txt', 'w') as f:
                #     f.write(str(self.order_number))
            
def main():
    """test"""
    cr = CashRegister('gardens_shop.json')
    # cr.scan_in()
    # cr.pay()
    # cr.receipt()
    cr.shop()
    # cr.reset_order()

if __name__ == "__main__":
    main()