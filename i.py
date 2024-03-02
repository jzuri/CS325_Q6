from abc import ABC, abstractmethod

# Interface for basic book search functionality
class Searchable:
    @abstractmethod
    def search_title(self, title):
        print("searching for book title")

    @abstractmethod
    def search_author(self, author):
        print("searching for book by author")

    @abstractmethod
    def search_genre(self, genre):
        print("searching for book by genre catagory")

class Borrowable:
    @abstractmethod
    def borrow_book(self, user_id, book_id):
        print("This book is out for use")

    @abstractmethod
    def return_book(self, user_id, book_id):
        print("This book has been returned")

class Reportable:
    @abstractmethod
    def borrowing_report(self):
        print("These books are currently out for renting")

    @abstractmethod
    def overdue_report(self):
        print("These books are overdue")

    @abstractmethod
    def popularity_report(self):
        print("These books are popular")

class Library(Searchable, Borrowable, Reportable):
    def __init__(self, catalog):
        self.catalog = catalog

    def search_title(self, title):
        print("searching for book title")

    def search_author(self, author):
        print("searching for book by author")

    def search_genre(self, genre):
        print("searching for book by genre catagory")

    def borrow_book(self, user_id, book_id):
        print("This book is out for use")

    def return_book(self, user_id, book_id):
        print("This book has been returned")

    def borrowing_report(self):
        print("These books are currently out for renting")

    def overdue_report(self):
        print("These books are overdue")

    def popularity_report(self):
       print("These books are popular")

# Class representing Guest User
class Guest(Searchable):
    def __init__(self, library):
        self.library = library

    def search_by_title(self, title):
        return self.library.search_title(title)

    def search_by_author(self, author):
        return self.library.search_author(author)

    def search_by_genre(self, genre):
        return self.library.search_genre(genre)

# Class representing Librarian User
class Librarian(Searchable, Borrowable, Reportable):
    def __init__(self, library):
        self.library = library

    def search_by_title(self, title):
        return self.library.search_title(title)

    def search_by_author(self, author):
        return self.library.search_author(author)

    def search_by_genre(self, genre):
        return self.library.search_genre(genre)

    def borrow_book(self, user_id, book_id):
        return self.library.borrow_book(user_id, book_id)

    def return_book(self, user_id, book_id):
        return self.library.return_book(user_id, book_id)

    def generate_borrowing_report(self):
        return self.library.borrowing_report()

    def generate_overdue_report(self):
        return self.library.overdue_report()

    def generate_popularity_report(self):
        return self.library.popularity_report()

def main():
    # Dummy implementation of Library and users
    library = Library(catalog={})
    guest = Guest(library)
    librarian = Librarian(library)

    # Usage examples
    guest.search_by_title("Harry Potter")
    librarian.borrowing_report()

if __name__ == "__main__":
    main()
