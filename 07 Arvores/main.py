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

class TreeProduct():
    def __init__(self):
        self.source = None

    def insert_product(self, id, name, amount):
        product = Product(id, name, amount)

        if self.source is None:
            self.source = Node(product)
        else:
            self._insert_product(product, self.source)

    def _insert_product(self, product, node):
        if product.id < node.product.id:
            if node.left is None:
                node.left = Node(product)
            else:
                self._insert_product(product, node.left)
        elif product.id > node.product.id:
            if node.right is None:
                node.right = Node(product)
            else:
                self._insert_product(product, node.right)
        else:
            node.product = product 

    def search_product(self, id):
        return self._search_product(id, self.source)

    