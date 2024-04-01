import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def test_set_book_genre_existent_genre(self,books_list):
        books_list.set_book_genre('Карлсон', 'Фантастика')
        assert books_list.get_book_genre('Карлсон') == 'Фантастика'

    @pytest.mark.parametrize('genre', ['НесуществующийЖанр', 'ТочноНесуществующийЖанр'])
    def test_set_book_genre_set_incorrect_genres(self, genre):
        collector = BooksCollector()

        collector.add_new_book('Тьма')
        collector.set_book_genre('Тьма', genre)

        assert collector.get_books_genre() == {'Тьма': ''}

    def test_get_book_genre_existing_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Карлсон')
        collector.set_book_genre('Карлсон', 'Мультфильмы')

        assert collector.get_book_genre('Карлсон') == 'Мультфильмы'

    def test_get_books_with_specific_genre_book_present(self):
        collector = BooksCollector()

        collector.add_new_book('Карлсон')
        collector.set_book_genre('Карлсон', 'Мультфильмы')

        assert 'Карлсон' in collector.get_books_with_specific_genre('Мультфильмы')


    def test_get_books_for_children_with_appropriate_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Карлсон')
        collector.set_book_genre('Карлсон', 'Мультфильмы')

        assert 'Карлсон' in collector.get_books_for_children()


    def test_get_books_for_children_with_inappropriate_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Ужасы нашего городка')
        collector.set_book_genre('Ужасы нашего городка', 'Ужасы')

        assert 'Ужасы нашего городка' not in collector.get_books_for_children()

    def test_add_book_in_favorites_added_book(self):
        collector = BooksCollector()

        collector.add_new_book('Карлсон')

        collector.add_book_in_favorites('Карлсон')

        assert collector.get_list_of_favorites_books() == ['Карлсон']

    def test_add_book_in_favorites_add_two_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Карлсон')
        collector.add_new_book('Карлсон2')
        collector.add_new_book('Карлсон3')
        collector.add_book_in_favorites('Карлсон')
        collector.add_book_in_favorites('Карлсон3')

        assert collector.get_list_of_favorites_books() == ['Карлсон', 'Карлсон3']

    def test_delete_book_from_favorites_book_removed_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Карлсон')
        collector.add_book_in_favorites('Карлсон')

        collector.delete_book_from_favorites('Карлсон')

        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_nonexisting_book(self):
        collector = BooksCollector()

        collector.add_new_book('Карлсон')
        collector.add_book_in_favorites('Карлсон')

        collector.delete_book_from_favorites('Малыш и Карлсон')


        assert collector.get_list_of_favorites_books() == ['Карлсон']


    def test_get_list_of_favorites_books_returns_favorites_list(self):
        collector = BooksCollector()

        collector.add_new_book('Карлсон')
        collector.add_new_book('Тьма')
        collector.add_book_in_favorites('Карлсон')
        collector.add_book_in_favorites('Тьма')

        favorites_books = collector.get_list_of_favorites_books()

        assert len(favorites_books) == 2

    def test_get_books_genre_returns_dict(self,books_list):
        books_genre = books_list.get_books_genre()

        assert len(books_genre) == 3





