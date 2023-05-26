class Book():
    def __init__(self, name, number_page):
        self.name = name
        self.name = number_page

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

    def