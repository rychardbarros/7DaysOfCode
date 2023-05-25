class Product():
    def __init__(self, bar_code, name, value, amount):
        self.bar_code = bar_code
        self.name = name
        self.value = value
        self.amount = amount
        self.next_product = None
        self.previous_product = None
