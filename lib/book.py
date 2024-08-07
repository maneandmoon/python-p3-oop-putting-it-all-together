#!/usr/bin/env python3
import ipdb
#     def test_has_title_and_page_count(self):
#         '''has the title and page_count passed into __init__, and values can be set to new instance.'''

    # def test_requires_int_page_count(self):
    #     '''prints "page_count must be an integer" if page_count is not an integer.'''


    # def test_can_turn_page(self):
    #     '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called'''

    # FAILED Book in book.py prints "page_count must be an integer" if page_count is not an integer. - AssertionError: assert '' == 'page_count m... an integer\n'

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


book = Book("And Then There Were None", 272)
book = Book("The World According to Garp", 69)

print(book.title)
# print(book.page._count)

# ipdb.set_trace()
