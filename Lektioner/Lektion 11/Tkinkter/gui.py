import tkinter as tk
from tkinter import messagebox

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

class LibraryApp:
    def __init__(self, root, library):
        self.library = library
        self.root = root
        self.root.title("Bibliotek")

        # Titel och författare fält
        self.title_label = tk.Label(root, text="Titel:")
        self.title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(root)
        self.title_entry.grid(row=0, column=1)

        self.author_label = tk.Label(root, text="Författare:")
        self.author_label.grid(row=1, column=0)
        self.author_entry = tk.Entry(root)
        self.author_entry.grid(row=1, column=1)

        # Knapp för att lägga till bok
        self.add_button = tk.Button(root, text="Lägg till bok", command=self.add_book)
        self.add_button.grid(row=2, column=0, columnspan=2)

        # Lista över böcker
        self.books_listbox = tk.Listbox(root, width=50)
        self.books_listbox.grid(row=3, column=0, columnspan=2)

        # Knapp för att ta bort vald bok
        self.remove_button = tk.Button(root, text="Ta bort vald bok", command=self.remove_book)
        self.remove_button.grid(row=4, column=0, columnspan=2)

        # Uppdatera listan över böcker
        self.update_books_list()

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()

        if title and author:
            book = Book(title, author)
            self.library.add_book(book)
            self.update_books_list()
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Fel", "Titel och författare krävs")

    def remove_book(self):
        selected_book = self.books_listbox.get(tk.ACTIVE)
        if selected_book:
            book_title = selected_book.split(" av ")[0]
            self.library.remove_book(book_title)
            self.update_books_list()
        else:
            messagebox.showwarning("Fel", "Ingen bok vald")

    def update_books_list(self):
        self.books_listbox.delete(0, tk.END)
        for book in self.library.get_books():
            self.books_listbox.insert(tk.END, str(book))


if __name__ == "__main__":
    root = tk.Tk()
    library = Library()
    app = LibraryApp(root, library)
    root.mainloop()
