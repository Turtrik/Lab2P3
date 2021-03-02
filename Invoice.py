class Invoice:

    def __init__(self):
        self.items = {}

    #Calculates the price * the quantity for each item in products
    #returns the total cost for all items
    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v['unit_price']) * int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price
