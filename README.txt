План по тестированию проекта ya_note.

Файл test_routes:

1) авторизованному пользователю доступны все страницы ✅
2) после создания, редактирования или удаления заметок пользователь перенаправляется на страницу done ✅
3) неавторизованный пользователь не имеет доступа к страницам создания, редактирования и удаления заметок ✅
4) пользователь не имеет доступа к страницам просмотра, редактирования или удаления заметок других авторов ✅


1c) Главная страница доступна анонимному пользователю.
2c) Аутентифицированному пользователю доступна страница со списком заметок notes/,
    страница успешного добавления заметки done/, страница добавления новой заметки add/.
3c) Страницы отдельной заметки, удаления и редактирования заметки доступны только автору заметки.
    Если на эти страницы попытается зайти другой пользователь — вернётся ошибка 404.
4c) При попытке перейти на страницу списка заметок, страницу успешного добавления записи,
    страницу добавления заметки, отдельной заметки, редактирования или удаления заметки
    анонимный пользователь перенаправляется на страницу логина.
5c) Страницы регистрации пользователей, входа в учётную запись и выхода из неё доступны всем пользователям.

Файл test_logic:
1) Пользователь не может редактировать, просматривать или удалять чужие заметки ✅
2) Анонимный пользователь не может редактировать, просматривать или удалять чужие заметки ✅

Файл test_content:

1) Заметки передаются в контекст шаблона в отсортированном по id виде ✅

