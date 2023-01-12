# api_final_yatube
api final yatube

## Описание
Этот проект реализует API к Yatube. Благодаря ему можно создавать, получать, обновлять и удалять публикации, а также комментарии к ним. Кроме того, можно подписываться на авторов.

## Установка

- Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/esfiro4ka/api_final_yatube.git

cd api_final_yatube
```

- Cоздать и активировать виртуальное окружение:

```
python3 -m venv env

source env/bin/activate
```

- Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

- Выполнить миграции:

```
python3 manage.py migrate
```

- Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов

- GET-запрос поста с id=5

```
GET /api/v1/posts/5/
```

- GET-запрос комментария c id=2 к посту с id=5

```
GET /api/v1/posts/5/comments/2/
```

- POST-запрос поста

```
POST /api/v1/posts/

Content-type: application/json

{
    "text": "Текст поста",
    "image": null,
    "group": null
}
```
