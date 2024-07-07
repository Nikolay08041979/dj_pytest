# [Тестирование Django-приложения](https://github.com/netology-code/dj-homeworks/tree/video/3.4-django-testing/django_testing)

## Функционал тест-кейсов:

✅ проверка получения первого курса (retrieve-логика): создаем курс через фабрику; строим урл и делаем запрос через тестовый клиент; проверяем, что вернулся именно тот курс, который запрашивали;

✅ проверка получения списка курсов (list-логика): аналогично — сначала вызываем фабрики, затем делаем запрос и проверяем результат; проверка фильтрации списка курсов по id:

✅ создаем курсы через фабрику, передать ID одного курса в фильтр, проверить результат запроса с фильтром; проверка фильтрации списка курсов по name;

✅ тест успешного создания курса: здесь фабрика не нужна, готовим JSON-данные и создаём курс; 

✅ тест успешного обновления курса:
сначала через фабрику создаём, потом обновляем JSON-данными;
тест успешного удаления курса.


## Измененя внесены:
✅ [../advertisements/models.py](https://github.com/Nikolay08041979/dj_api_with_restrictions/blob/master/3.3-permissions/api_with_restrictions/advertisements/models.py)

✅ [../advertisement/admin.py](https://github.com/Nikolay08041979/dj_api_with_restrictions/blob/master/3.3-permissions/api_with_restrictions/advertisements/admin.py)

✅ [../advertisement/views.py](https://github.com/Nikolay08041979/dj_api_with_restrictions/blob/master/3.3-permissions/api_with_restrictions/advertisements/views.py)

✅ [../advertisements/serializers.py](https://github.com/Nikolay08041979/dj_api_with_restrictions/blob/master/3.3-permissions/api_with_restrictions/advertisements/serializers.py)

✅ [../advertisements/filters.py](https://github.com/Nikolay08041979/dj_api_with_restrictions/blob/master/3.3-permissions/api_with_restrictions/advertisements/filters.py)

✅ [../api_with_restrictions/urls.py](https://github.com/Nikolay08041979/dj_api_with_restrictions/blob/master/3.3-permissions/api_with_restrictions/api_with_restrictions/urls.py)

✅ [../api_with_restrictions/settings.py](https://github.com/Nikolay08041979/dj_api_with_restrictions/blob/master/3.3-permissions/api_with_restrictions/api_with_restrictions/settings.py)