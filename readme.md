# [Backend для приложения с объявлениями"](https://github.com/netology-code/dj-homeworks/tree/video/3.3-permissions/api_with_restrictions)

## Функционал:
✅ Реализовать бэкенд для мобильного приложения с объявлениями. Объявления можно создавать и просматривать. Есть возможность фильтровать объявления по дате и статусу.

✅ Создавать могут только авторизованные пользователи. Для просмотра объявлений авторизация не нужна.

✅ У объявления есть статусы: OPEN, CLOSED. Необходимо валидировать, что у пользователя не больше 10 открытых объявлений.

✅ Обновлять и удалять объявление может только его автор.

✅ Чтобы боты и злоумышленники не нагружали нашу систему, добавьте лимиты на запросы: для неавторизованных пользователей: 10 запросов в минуту; для авторизованных пользователей: 20 запросов в минуту.


## Измененя внесены:
✅ [advertisements/models.py](https://github.com/Nikolay08041979/dj_api_with_restrictions/blob/master/3.3-permissions/api_with_restrictions/advertisements/models.py)

✅ [advertisement/admin.py](https://github.com/Nikolay08041979/dj_api_with_restrictions/blob/master/3.3-permissions/api_with_restrictions/advertisements/admin.py)

✅ [advertisement/views.py](https://github.com/Nikolay08041979/dj_api_with_restrictions/blob/master/3.3-permissions/api_with_restrictions/advertisements/views.py)

✅ [advertisements/serializers.py]https://github.com/Nikolay08041979/dj_api_with_restrictions/blob/master/3.3-permissions/api_with_restrictions/advertisements/serializers.py

✅ [advertisements/filters.py](https://github.com/Nikolay08041979/dj_api_with_restrictions/blob/master/3.3-permissions/api_with_restrictions/advertisements/filters.py)

✅ [api_with_restrictions/urls.py](https://github.com/Nikolay08041979/dj_api_with_restrictions/blob/master/3.3-permissions/api_with_restrictions/api_with_restrictions/urls.py)

✅ [api_with_restrictions/settings.py]https://github.com/Nikolay08041979/dj_api_with_restrictions/blob/master/3.3-permissions/api_with_restrictions/api_with_restrictions/settings.py