class Book():
    def __init__(self, name, number_page):
        self.name = name
        self.number_page = number_page

class ListBook():
    def __init__(self):
        self.pile_books = []

    def add_book(self, name, number_page):
        new_book = Book(name, number_page)
        self.pile_books.append(new_book)

    def remove_book(self):
        if len(self.pile_books) < 1:
            return None
        return self.pile_books.pop()

    def list_book_top(self):
        index = len(self.pile_books) - 1
        print(f'O livro do topo é: {self.pile_books[index]}')
        return self.pile_books[index]

    def book_list(self):
        if len(self.pile_books) < 1:
            print('Não há livros na pilha no momento')
            return
        else:
            for book in self.pile_books:
                print(f'Nome: {book.name}, número de páginas: {book.number_page}')

    