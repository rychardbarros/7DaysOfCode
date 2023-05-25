class Product():
    def __init__(self, bar_code, name, value, amount):
        self.bar_code = bar_code
        self.name = name
        self.value = value
        self.amount = amount
        self.next_product = None
        self.previous_product = None

class ListProduct():
    def __init__(self):
        self.head = None
        self.tail = None

    def add_product(self, bar_code, name, value, amount):
        new_product = Product(bar_code, name, value, amount)
        if self.head is None:
            self.head = new_product
            self.tail = new_product
        else:
            self.tail.next_product = new_product
            new_product.previous_product = self.tail
            self.tail = new_product

    def remove_product(self, bar_code):
        if self.head is None:
            return
        elif self.head.bar_code == bar_code:
            self.head = self.head.next_product
            if self.head is not None:
                self.head.previous_product = None
            else:
                self.tail = None
        elif self.tail.bar_code == bar_code:
            self.tail = self.tail.previous_product
            self.tail.next_product = None
            return
        
            
