# [Backend для приложения с объявлениями"](https://github.com/netology-code/dj-homeworks/tree/video/3.3-permissions/api_with_restrictions)

## Функционал:
✅ Реализовать бэкенд для мобильного приложения с объявлениями. Объявления можно создавать и просматривать. Есть возможность фильтровать объявления по дате и статусу.

✅ Создавать могут только авторизованные пользователи. Для просмотра объявлений авторизация не нужна.

✅ У объявления есть статусы: OPEN, CLOSED. Необходимо валидировать, что у пользователя не больше 10 открытых объявлений.

✅ Обновлять и удалять объявление может только его автор.

✅ Чтобы боты и злоумышленники не нагружали нашу систему, добавьте лимиты на запросы: для неавторизованных пользователей: 10 запросов в минуту; для авторизованных пользователей: 20 запросов в минуту.


### Измененя внесены:
✅ [school/modele.py](https://github.com/Nikolay08041979/django_project-4/blob/master/orm_migrations/school/models.py)

✅ [school/admin.py](https://github.com/Nikolay08041979/django_project-4/blob/master/orm_migrations/school/admin.py)

✅ [school/views.py](https://github.com/Nikolay08041979/django_project-4/blob/master/orm_migrations/school/views.py)

✅ [templates/school/student_list.html](https://github.com/Nikolay08041979/django_project-4/blob/master/orm_migrations/templates/school/students_list.html)