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
        gross_income = sum(income)
        return gross_income

    def total_tax_owed(self):
        """totals tax owed from receipts"""
        tax = []
        receipts = read_json(self.file_name)
        for d in receipts:
            tax.append(d['tax'])
        tax_owed = sum(tax)
        return tax_owed

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