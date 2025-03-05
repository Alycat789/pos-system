from handy_functions import read_json

class Calculator:
    """Calculates prices and tax totals"""

    def __init__(self) -> None:
        self.subtotal = 0
        self.tax_percent = 6
        self.tax = 0
        self.total = 0
        
#TODO: Make the decimals stop at the hundredth's place. Account for rounding error Scott told you about.
    def calc_subtotal(self):
        """adds all prices together"""
        order = read_json('order.json')
        sub_list = []
        for d in order:
            sub_list.append(float(d['price']))
        self.subtotal = sum(sub_list)
        return round(self.subtotal, 2)

    def calc_tax(self):
        """applies tax to subtotal"""
        tax_rate = self.tax_percent/100
        self.tax = tax_rate * self.subtotal
        return round(self.tax, 2)

    def calc_total(self):
        """adds tax to total"""
        sub = self.calc_subtotal()
        tax = self.calc_tax()
        self.total = sub + tax
        return self.total
    
def main():
    """test"""
    c = Calculator()
    print(c.calc_subtotal())
    print(c.calc_tax())
    print(c.calc_total())

if __name__ == "__main__":
    main()