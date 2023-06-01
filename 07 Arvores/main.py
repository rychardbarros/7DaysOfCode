class Product():
    def __init__(self, id, name, amount):
        self.id = id
        self.name = name
        self.amount = amount

class Node():
    def __init__(self, product):
        self.right = None
        self.left = None
        self.product = product
