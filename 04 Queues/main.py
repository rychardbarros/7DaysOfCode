class Order():
    def __init__(self, number, name, food, table):
        self.number = number
        self.name = name
        self.food = food
        self.table = table

class ListOrder():
    def __init__(self):
        self.list_order = []

    def add_order(self, number, name, food, table):
        new_order = Order(number, name, food, table)
        self.list_order.append(new_order)

    def remove_order(self):
        if len(self.list_order) < 1:
            print('Não há pedidos no momento!')
            return 
        else:
            return self.list_order.pop(0)

    def order_list(self):
        if len(self.list_order) < 1:
            print('Não há pedidos no momento!')
            return
        else:
            for order in self.list_order:
                print(f'Numero:{order.number} Nome: {order.name} | Prato: {order.food} | Mesa:{order.table}')

list_order = ListOrder()

list_order.add_order('01','Rychard','Pizza, Batata Frita', '5')
list_order.add_order('02', 'João', 'Hambúrguer', '6')
list_order.add_order('03', 'Marcio', 'Pastel', '7')

list_order.order_list()

list_order.remove_order()

list_order.order_list()