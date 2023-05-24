class ShoppingList():
    def __init__(self):
        self.items = []
        self.amounts = []

    def add_item(self, item, amount):
        self.items.append(item)
        self.amounts.append(amount)

    def remove_item(self, item):
        index = self.items.index(item)
        self.items.pop(index)
        self.amounts.pop(index)

    def list_items(self):
        print('Lista de Compras')
        for i in range(len(self.items)):
            print(f'{self.items[i]}: {self.amounts[i]}')

shopping_list = ShoppingList()


shopping_list.add_item('Arroz', '1')
shopping_list.add_item('Pão', '4')
shopping_list.add_item('Café', '37')
shopping_list.add_item('Energético', '2')

shopping_list.list_items()

shopping_list.remove_item('Arroz')

shopping_list.list_items()