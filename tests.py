import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_books_genre_initialization_empty_dict(self):
        collector = BooksCollector()

        # проверяем, что изначально инициализируемый словарь пуст
        assert isinstance(collector.books_genre, dict) and len(collector.books_genre) == 0

    def test_favorites_initialization_empty_list(self):
        collector = BooksCollector()

        # проверяем, что изначально инициализируемый список избранного пуст
        assert isinstance(collector.favorites, list) and len(collector.favorites) == 0

    def test_genre_initialization_list_5(self):
        collector = BooksCollector()

        # проверяем, что в инициализируемом списке жанров 5 жанров
        assert len(collector.genre) == 5

    def test_genre_age_rating_initialization_list_2(self):
        collector = BooksCollector()

        # проверяем, что в инициализируемом списке жанров для взрослых 2 жанра
        assert len(collector.genre_age_rating) == 2

    def test_add_new_book_one_book_success(self):
        collector = BooksCollector()

        collector.add_new_book('Собака Баскервилей')
        # проверяем, что книга добавлена в список книг
        assert 'Собака Баскервилей' in collector.books_genre

    def test_add_new_book_add_two_books_success(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name',
                             ['A', 'A' * 40, 'The Hound of the Baskervilles', '1', '@'])
    def test_add_new_book_valid_name_success(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        # проверяем, что книга добавляется с разным набором имен
        assert len(collector.books_genre) == 1

    def test_add_new_book_double_book_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('Собака Баскервилей')
        collector.add_new_book('Собака Баскервилей')
        # проверяем, что дубль книги не добавляется в список книг
        assert len(collector.books_genre) == 1

    def test_add_new_book_empty_name_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('')
        # проверяем, что книга не добавляется с пустым именем
        assert len(collector.books_genre) == 0

    def test_add_new_book_name_eql_41_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('A' * 41)
        # проверяем, что книга не добавляется с именем в 41 символ
        assert len(collector.books_genre) == 0

    def test_set_book_genre_set_valid_genre_success(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, 'Детективы')
        # проверяем, что жанр успешно добавлен к существующей книге
        assert collector.books_genre.get(new_book) == 'Детективы'

    @pytest.mark.parametrize('genre',
                             ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_set_all_valid_genre_success(self, genre):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, genre)
        # проверяем, что каждый жанр успешно добавлен к существующей книге
        assert collector.books_genre.get(new_book) == genre

    def test_set_book_genre_different_genre_changed_last_genre(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, 'Детективы')
        collector.set_book_genre(new_book, 'Комедии')
        # проверяем, что внесения изменения жанра к одной книге успешно
        assert collector.books_genre.get(new_book) == 'Комедии'

    def test_set_book_genre_invalid_genre_not_added_genre(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, 'Детективчик')
        # проверяем, что несуществующий жанр в списке не добавится к книге
        assert collector.books_genre.get(new_book) == ''

    def test_set_book_genre_nonexistent_book_not_added_book(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.set_book_genre(new_book, 'Детективы')
        # проверяем, что жанр не добавится к несуществующей книге
        assert len(collector.books_genre) == 0

    def test_set_book_genre_same_genre_not_added_double(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, 'Детективы')
        collector.set_book_genre(new_book, 'Детективы')
        # проверяем, что несколько добавлений того-же жанра к книге не задублируют книгу
        assert len(collector.books_genre) == 1

    def test_set_book_genre_same_genre_not_changed_genre(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, 'Детективы')
        collector.set_book_genre(new_book, 'Детективы')
        # проверяем, что несколько добавлений того-же жанра к книге не повлияет на жанр
        assert collector.books_genre.get(new_book) == 'Детективы'

    def test_get_book_genre_one_book_success(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        genre = 'Детективы'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, genre)
        # проверяем, что жанр запрашивается корректно, при существующей книги с жанром
        assert collector.get_book_genre(new_book) == genre

    @pytest.mark.parametrize('book, genre',
                             [
                                 ('Блэксэд', 'Фантастика'),
                                 ('Мизери', 'Ужасы'),
                                 ('Собака Баскервилей', 'Детективы'),
                                 ('Снег на траве', 'Мультфильмы'),
                                 ('Как важно быть серьезным', 'Комедии')
                             ])
    def test_get_book_genre_all_valid_genre_success(self, book, genre):
        collector = BooksCollector()

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    def test_get_book_genre_nonexistent_book_is_none(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        # проверяем, что вернется None, если запрашиваемой книги не существует
        assert collector.get_book_genre(new_book) is None

    def test_get_book_genre_book_without_genre_is_empty_genre(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        # проверяем, что жанр будет пустой, если у книги не назначен жанр
        assert collector.get_book_genre(new_book) == ''


    @pytest.mark.parametrize('book, genre',
                             [
                                 ('Блэксэд', 'Фантастика'),
                                 ('Мизери', 'Ужасы'),
                                 ('Собака Баскервилей', 'Детективы'),
                                 ('Снег на траве', 'Мультфильмы'),
                                 ('Как важно быть серьезным', 'Комедии')
                             ])
    def test_get_books_with_specific_genre_all_valid_genres_success(self, book, genre):
        collector = BooksCollector()

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        # проверяем, что каждый жанр возвращает соответсвующую книгу
        assert collector.get_books_with_specific_genre(genre) == [book]


    @pytest.mark.parametrize('genre',
                             [
                                 'Фантастика',
                                 'Ужасы',
                                 'Детективы',
                                 'Мультфильмы',
                                 'Комедии'
                             ])
    def test_get_books_with_specific_genre_with_multiple_all_genres_success(self, genre):
        collector = BooksCollector()

        new_book = 'Книга'
        collector.add_new_book(new_book)
        collector.add_new_book(new_book + '-2')

        collector.set_book_genre(new_book, genre)
        collector.set_book_genre(new_book + '-2', genre)
        # проверяем, что метод возвращает все книги с каждым жанром, если их несколько
        assert collector.get_books_with_specific_genre(genre) == [new_book, new_book + '-2']

    def test_get_books_with_specific_genre_with_nonexistent_genre_is_list_empty(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, 'Детективы')
        # проверяем, что метод возвращает пустой список, если нет такого жанра
        assert collector.get_books_with_specific_genre('Неизвестный жанр') == []

    def test_add_book_in_favorites_valid_book_with_genre_success(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, 'Детективы')
        collector.add_book_in_favorites(new_book)
        # проверяем, что книга с жанром корректно добавляется в список избранного
        assert 'Собака Баскервилей' in collector.favorites

    def test_add_book_in_favorites_valid_book_without_genre_success(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.add_book_in_favorites(new_book)
        # проверяем, что книга без жанра корректно добавляется в список избранного
        assert 'Собака Баскервилей' in collector.favorites

    def test_add_book_in_favorites_two_books(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.add_book_in_favorites(new_book)
        collector.add_new_book(new_book + '-2')
        collector.add_book_in_favorites(new_book + '-2')
        # проверяем, что две книги корректно добавляются в список избранного
        assert len(collector.favorites) == 2

    def test_add_book_in_favorites_nonexistent_book_is_empty_list(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Несуществующая книга')
        # проверяем, что несуществующая книга не добавляется в избранное
        assert collector.favorites == []

    def test_add_book_in_favorites_add_double_book_not_added(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.add_book_in_favorites(new_book)
        collector.add_book_in_favorites(new_book)
        # проверяем, что одна и та же книга не добавится в список избранного повторно
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_valid_book_success(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.add_book_in_favorites(new_book)

        # проверяем, что метод удаляет книгу из избранного
        collector.delete_book_from_favorites(new_book)
        assert collector.favorites == []

    def test_delete_book_from_favorites_valid_one_book_success(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.add_book_in_favorites(new_book)
        collector.add_new_book(new_book + '-2')
        collector.add_book_in_favorites(new_book + '-2')

        # проверяем, что метод удаляет книгу из избранного, где в списке несколько книг
        collector.delete_book_from_favorites(new_book)
        assert new_book not in collector.favorites and new_book + '-2' in collector.favorites

    def test_delete_book_from_favorites_nonexistent_book_not_deleted(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.add_book_in_favorites(new_book)
        # проверяем, что метод не удаляет несуществующую книгу
        collector.delete_book_from_favorites('Несуществующая книга')
        assert new_book in collector.favorites

    def test_get_list_of_favorites_books_with_one_book_success(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.add_book_in_favorites(new_book)
        # проверяем, что метод возвращает список избранного из одной книги
        assert collector.get_list_of_favorites_books() == [new_book]

    def test_get_list_of_favorites_books_with_two_book_success(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.add_book_in_favorites(new_book)
        collector.add_new_book(new_book + '-2')
        collector.add_book_in_favorites(new_book + '-2')
        # проверяем, что метод возвращает список избранного из двух книг
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_get_list_of_favorites_books_after_deleted_book_is_empty_list(self):
        collector = BooksCollector()

        new_book = 'Собака Баскервилей'
        collector.add_new_book(new_book)
        collector.add_book_in_favorites(new_book)
        collector.delete_book_from_favorites(new_book)

        # проверяем, что метод возвращает пустой список после удаления книги из избранного
        assert collector.get_list_of_favorites_books() == []

