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

    def _search_product(self, id, node):
        if node is None or node.product.id == id:
            return node
        elif id < node.product.id:
            return self._search_product(id, node.left)
        else:
            return self._search_product(id, node.right)

tree = TreeProduct()

tree.insert_product(1, 'Tenis', '10')
tree.insert_product(2, 'Camiseta', '15')
tree.insert_product(3, 'Calça', '7')

product_01 = tree.search_product(2)

if product_01 is not None:
    print(f'Product ID: {product_01.product.id} \nProduct Name: {product_01.product.name} \nProduct Amount: {product_01.product.amount}')
else:
    print("Product not found.")

product_02 = tree.search_product(5)
print(product_02) # retorna None



    