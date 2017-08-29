import unittest

from Book_Shop.Books import Books


class TestBooks(unittest.TestCase):



    def setUp(self):
        self.buf = Books()

    def tearDown(self):
        del self.buf

    def test_CreateBook(self):
        test_book = {
            "ID": '1',
            "Author": 'Andrew',
            "Name": 'AA',
            "Year": '1234'
        }
        self.buf.createBook(author=test_book.get('Author'), name=test_book.get('Name'), year=test_book.get('Year'))
        self.assertEqual(self.buf.books, [{'id': test_book.get('ID'), 'author': test_book.get('Author'),
                                           'name': test_book.get('Name'), 'year': test_book.get('Year')}] )

    def test_DeleteBook(self):
        test_book = {
            "ID": '1',
            "Author": 'Andrew',
            "Name": 'AA',
            "Year": '1234'
        }
        self.buf.createBook(author=test_book.get('Author'), name=test_book.get('Name'), year=test_book.get('Year'))
        self.buf.deleteBookById(id=test_book.get('ID'))
        self.assertEqual(len(self.buf.books), 0)

    def test_SaveFile(self):
        pass

    def test_SearchIdBook(self):
        test_book = {
            "ID": '1',
            "Author": 'Andrew',
            "Name": 'AA',
            "Year": '1234'
        }
        self.buf.createBook(author=test_book.get('Author'), name=test_book.get('Name'), year=test_book.get('Year'))
        self.buf.createBook(author=test_book.get('Author'), name=test_book.get('Name'), year=test_book.get('Year'))
        self.buf.searchBook_ID(test_book.get('ID'))
        self.assertEqual(self.buf.found_book[0]['id'], test_book.get('ID'))

    def test_SearchAuthorBook(self):
        self.buf.createBook(author='Andrew', name='AAA', year='1234')
        self.buf.createBook(author='Lena', name='LLL', year='4321')
        self.buf.searchBook_author('Andrew')
        self.assertEqual(self.buf.found_book[0]['author'], 'Andrew')

    def test_SearchNameBook(self):
        self.buf.createBook(author='Andrew', name='AAA', year='1234')
        self.buf.createBook(author='Lena', name='LLL', year='4321')
        self.buf.searchBook_name('LLL')
        self.assertEqual(self.buf.found_book[0]['name'], 'LLL')


    def test_SearchYearBook(self):
        self.buf.createBook(author='Andrew', name='AAA', year='1234')
        self.buf.createBook(author='Lena', name='LLL', year='4321')
        self.buf.searchBook_year('1234')
        self.assertEqual(self.buf.found_book[0]['year'], '1234')

if __name__ == '__main__':
    unittest.main()