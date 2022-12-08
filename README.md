# Currency-ETL

##Задача
Реализация API для получения курса валют, разработать интеграцию с API курса валют

##Решение
Реализована функция для интеграции с API курса валют, ежедневный запуск осуществляется с помощью триггера.
Данные хранятся в базе данных, доступ к которым можно получить через API для получения курса валют на указанную дату.
Валидация данных осуществляется с помощью библиотеки Pydantic


##Технологии
FastApi, Postgresql, SQLAlchemy, Yandex Functions


##Процесс сборки
Зарегистироваться в Yandex registry
```shell
docker login --username oauth --password <YOUR_YANDEX_OATH_TOKEN> cr.yandex
```

Билд FastAPI приложения
```shell
cd app/
docker build -t yandex_api .
```
Добавить тэг
```shell
docker tag yandex_api cr.yandex/<YOUR_REGISTRY_ID>/yandex_api:latest
```
Опубликовать образ
```shell
docker push cr.yandex/<YOUR_REGISTRY_ID>/yandex_api
```

##Работа с приложением
1) Зарегестрировать пользователя через POST запрос на /user/signup
2) Получить токен через /user/login
3) Post запрос на /connect сохраняет в бд курсы на указанную дату
4) Get запрос на /connect получает данные из бд на указанную в параметре date дату

##Переменные окружения
####SQLALCHEMY_URL - урл дляподключения к бд
####POSTGRES_DBNAME - имя бд
####POSTGRES_USER - имя пользователя бд
#####POSTGRES_PASSWORD - пароль бд
####FUNCTION_URL - урл яндекс функции
####SECRET_KEY - ключ для кодирования токена
####ALGORITHM - алгоритм кодирования для токена
