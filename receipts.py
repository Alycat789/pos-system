import os
from handy_functions import read_json, load_json
ROOT_DIR = os.path.dirname(__file__)

class Receipts:
    """compiles info from receipt.json, and deletes it."""

    def __init__(self) -> None:
        self.file_name = 'receipts.json'
        self.file_path = os.path.join(self.file_name)

    def total_income(self):
        """totals gross income from receipts"""
        income = []
        receipts = read_json(self.file_name)
        for d in receipts:
            income.append(d['total'])
        print(income)
        gross_income = sum(income)
        print("gross income: ", gross_income)
        return round(gross_income, 2)

    def total_tax_owed(self):
        """totals tax owed from receipts"""
        tax = []
        receipts = read_json(self.file_name)
        for d in receipts:
            tax.append(d['tax'])
        print(tax)
        tax_owed = sum(tax)
        print("tax owed: ", tax_owed)
        return round(tax_owed, 2)

    def delete_receipts(self):
        """deletes receipts"""
        os.remove(self.file_path)
        load_json('receipts.json', [])

def main():
    """tests"""
    r = Receipts()
    # r.delete_receipts()
    print(r.total_income())
    print(r.total_tax_owed())

if __name__ == "__main__":
    main()