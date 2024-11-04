# Задача:
# Создадим класс BookCollection, который будет представлять коллекцию книг,
# и добавим к нему итератор. Итератор позволит поочередно перебрать все книги в коллекции.
# Автор: Соколов Е.А. 43ИС-21


# класс представляющий книгу
class Book:
    def __init__(self, title):
        self.title = title

class BookCollection:
    def __init__(self):
        self.books = []

    # метод для добавления книги в коллекцию
    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        return BookIterator(self.books)

class BookIterator:
    def __init__(self, books):
        self._books = books
        self._index = 0

    # метод возвращает следующую книгу или вызывает исключение
    def __next__(self):
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration

# используем паттерн Итератор
collection = BookCollection()
collection.add_book(Book("Над пропастью во ржи"))
collection.add_book(Book("Убить пересмешника"))
collection.add_book(Book("1984"))

for book in collection:
    print(book.title)
