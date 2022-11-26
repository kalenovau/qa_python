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
    # Проверяем что не добавляется дубликат книги
    def test_add_new_book_duplicate_false(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Майор гром')
        collector.add_new_book('Война и мир')
        assert len(collector.get_books_rating()) == 2

    # Проверяем что при добавлении книги присваивается рейтинг 1
    def test_add_new_book_rating_is_1(self):
        collector = BooksCollector()
        collector.add_new_book('Чук и Гек')
        collector.add_new_book('Джейн Эйр')
        assert collector.books_rating['Чук и Гек'] == 1

    # Проверяем что можем присвоить рейтинг книге
    def test_set_book_rating_is_6(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка на Луне')
        collector.add_new_book('Приключения Буратино')
        collector.set_book_rating('Незнайка на Луне', 6)
        assert collector.books_rating['Незнайка на Луне'] == 6

    # Проверяем что не можем присвоить рейтинг книге, которой нет в списке
    def test_set_book_rating_not_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Три богатыря')
        collector.add_new_book('Царевна-лягушка')
        assert collector.set_book_rating('Огниво', 6) == None

    # Проверяем что не можем присвоить книге рейтинг меньше 1
    def test_set_book_rating_smaller_than_1(self):
        collector = BooksCollector()
        collector.add_new_book('Мы')
        collector.add_new_book('1984')
        collector.set_book_rating('Мы', 0)
        assert collector.set_book_rating('Незнайка на Луне', 0) == None

    # Проверяем что можем посмотреть рейтинг книги по ее имени
    def test_get_book_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Бойцовский клуб')
        collector.add_new_book('Заводной апельсин')
        collector.set_book_rating('Бойцовский клуб', 6)
        assert collector.get_book_rating('Заводной апельсин')

    # Проверяем что можем получить список книг с определенным рейтингом
    def test_get_books_with_specific_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Каштанка')
        collector.add_new_book('Тараканище')
        collector.add_new_book('Три поросенка')
        collector.set_book_rating('Каштанка', 6)
        assert len(collector.get_books_with_specific_rating(1)) == 2

    # Проверяем возможность вывести словарь
    def test_get_books_rating(self):
        collector = BooksCollector()
        collector.add_new_book('На дне')
        collector.add_new_book('Гранатовый браслет')
        collector.add_new_book('Старуха Изергиль')
        assert collector.get_books_rating()

    # Проверяем добавление книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Как закалялась сталь')
        collector.add_new_book('Мальчиш Кибальчиш')
        collector.set_book_rating('Как закалялась сталь', 6)
        collector.add_book_in_favorites('Как закалялась сталь')
        assert 'Как закалялась сталь' in collector.favorites

    # Проверяем удаление книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Что такое хорошо')
        collector.add_new_book('Дядя Степа')
        collector.add_book_in_favorites('Что такое хорошо')
        assert 'Что такое хорошо' in collector.favorites
        collector.delete_book_from_favorites('Что такое хорошо')
        assert 'Что такое хорошо' not in collector.favorites

    # Проверяем что выводится список избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дядя Федор, пес и кот')
        collector.add_new_book('Зима в Простоквашино')
        collector.add_new_book('Каникулы в Простоквашино')
        collector.add_book_in_favorites('Зима в Простоквашино')
        collector.add_book_in_favorites('Каникулы в Простоквашино')
        assert collector.get_list_of_favorites_books()

    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()