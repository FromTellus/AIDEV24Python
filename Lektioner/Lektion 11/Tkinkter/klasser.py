class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} av {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        self.books = [book for book in self.books if book.title != book_title]

    def get_books(self):
        return self.books
