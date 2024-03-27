# qa_python
## Приложение BooksCollector 
Приложение позволяет установить жанр книг и добавить их в избранное.

### Класс BooksCollector содержит:
Словарь books_genre, куда можно добавить пару Название книги: Жанр книги.
Список favorites, который содержит избранные книги.
Список genre, который содержит доступные жанры.
Список genre_age_rating, который содержит жанры с возрастным рейтингом.
#### Набор методов для работы со словарем books_genre и списком favorites:
1. add_new_book — добавляет новую книгу в словарь без указания жанра. Название книги может содержать максимум 40 символов. Одну и ту же книгу можно добавить только один раз.
2. set_book_genre — устанавливает жанр книги, если книга есть в books_genreи её жанр входит в списокgenre.
3. get_book_genre— выводит жанр книги по её имени.
4. get_books_with_specific_genre— выводит список книг с определённым жанром.
5. get_books_genre— выводит текущий словарь books_genre.
6. get_books_for_children — возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга.
7. add_book_in_favorites — добавляет книгу в избранное. Книга должна находиться в словаре books_genre. Повторно добавить книгу в избранное нельзя.
8. delete_book_from_favorites — удаляет книгу из избранного, если она там есть.
9. get_list_of_favorites_books — получает список избранных книг.
 

#### тесты, которые удалось реализовать:

1. test_set_book_genre_existent_genre - существующий жанр устанавливается
2. test_set_book_genre_nonexistent_genre - несуществующий жанр не устанавливается
3. test_get_book_genre_existing_genre - возвращается установленный жанр
4. test_get_books_with_specific_genre_book_present - книга с установленным жанром присутствует в списке книг с этим жанром
5. test_get_book_genre_with_existing_genre
6. test_get_books_for_children_with_appropriate_genre
7. test_get_books_for_children_with_inappropriate_genre
8. test_add_book_in_favorites_added_book
9. test_add_book_in_favorites_add_two_book_in_favorites
10. test_delete_book_from_favorites_book_removed_from_favorites
11. test_delete_nonexisting_book_from_favorites
12. test_delete_book_from_favorites_delete_books
13. test_set_book_genre_set_incorrect_genres   