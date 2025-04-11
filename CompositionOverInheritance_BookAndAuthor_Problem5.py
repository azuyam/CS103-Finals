""" Composition Over Inheritance: Create a Book class with a Author class included within it, demonstrating composition over inheritance. """

class Author:

    # This is the class representing an author of a book.

    def __init__(self, name, birth_year):
        
        self.name = name
        self.birth_year = birth_year

    def get_author_info(self):

        return f"{self.name}, born in {self.birth_year}"


class Book:

    # This is the class representing a book, which contains an author.
    
    def __init__(self, title, author):

        self.title = title
        self.author = author  # Demonstrates Composition because Book has an Author

    def get_book_info(self):

        return f"'{self.title}' by {self.author.get_author_info()}"


# OUTPUT HERE. WITH RESPECTIVE INSTANCES AND PRINT THE OUTPUT AFTERWARDS.
if __name__ == "__main__":

    author = Author("Fyodor Dostoevsky", 1821)

    book = Book("The House of the Dead", author)
    
    print(book.get_book_info())

    