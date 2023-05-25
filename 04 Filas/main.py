class Order():
    def __init__(self, number, name, food):
        self.number = number
        self.name = name
        self.food = food

class ListOrder():
    def __init__(self):
        self.list_order = []

    def add_order(self, number, name, food):
        new_order = Order(number, name, food)
        self.list_order.append(new_order)

    def remove_order(self):
        if len(self.list_order) < 1:
            print('Não há pedidos no momento!')
            return 
        else:
            return self.list_order.pop(0)

    def list_order(self):
        if len(self.list_order) < 1:
            print('Não há pedidos no momento!')
            return
        else:
            for order in self.list_order:
                print(f'Numero:{order.number}, Nome: {order.name}, Prato:{order.food}')

list_order = ListOrder()
