# Блог от Лизы

Блог на Django, серверная часть.

## Запуск

Для запуска блога у вас уже должен быть установлен Python 3.

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Запустите сервер командой `python3 manage.py runserver`

После этого переходите по ссылке [127.0.0.1:8000](http://127.0.0.1:8000), вы увидите главную страницу.

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

**Для запуска проекта эти настройки не требуются**, значения уже проставлены по умолчанию.

Доступны следущие переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.
- `SECRET_KEY` — секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`.
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `STATIC_URL` — по умолчанию это `'/static/'`. [Что такое STATIC_URL](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-STATIC_URL).
- `STATIC_ROOT` — по умолчанию это `'None'`, т.е. текущая папка. [Что такое STATIC_ROOT](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-STATIC_ROOT).
- `MEDIA_URL` — по умолчанию это `'/media/'`. [Что такое MEDIA_URL](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-MEDIA_URL).
- `MEDIA_ROOT` — по умолчанию это `'media'`. [Что такое MEDIA_ROOT](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-MEDIA_ROOT). 


## Страницы сайта

### Главная

Страница называется `index` и находится по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

Шаблон страницы получает 2 переменные: `most_popular_posts` и `fresh_posts`.
Обе переменные — это списки из **постов**. Каждый пост — это словарь такого вида:

```
{
    'title': 'Are You Preparing Your Kids for the Real World?',
    'text': 'We baby our kids like infants; we coddle them like delicate crystal; ...',
    'author': 'Frank Sonnenberg',
    'comments_amount': 138,
    'image_url': 'image_are-you-preparing-your-kids-for-the-real-world.jpg',
    'published_at': datetime.datetime(2017, 6, 4, 2, 9, tzinfo=<UTC>),
    'slug': 'are-you-preparing-your-kids-for-the-real-world'
}
```

Словарь содержит следующие ключи:

* `title` — заголовок поста
* `text` — текст поста
* `author` — строка с именем автора поста
* `comments_amount` — число комментариев под постом
* `image_url` — ссылка на картинку поста
* `published_at` — когда пост опубликован, это объект datetime
* `slug` — [слаг](https://toster.ru/q/375615)



### Страница поста

Страница называется `post_detail` и требует передать `slug` поста. Пример страницы можно найти по адресу [http://127.0.0.1:8000/post/5-qualities-of-great-leaders](http://127.0.0.1:8000/post/5-qualities-of-great-leaders). Это страница поста со слагом `5-qualities-of-great-leaders`.

Шаблон страницы получает переменную: `post`.

`post` — это словарь, похожий на посты на главной, но с отличиями:

* `title` — заголовок поста
* `text` — текст поста
* `author` — строка с именем автора поста
* `comments` — **список комментариев** (о них ниже)
* `likes_amount` — число лайков под постом
* `image_url` — ссылка на картинку поста
* `published_at` — когда пост опубликован, это объект datetime
* `slug` — [слаг](https://toster.ru/q/375615)

Каждый **комментарий** — это словарь вида:

* `text` — текст комментария
* `published_at` — когда пост опубликован, это объект datetime
* `author` — строка с именем автора поста

### Контакты

Страница называется `contact`.

Её можно найти по адресу [127.0.0.1:8000/contacts](127.0.0.1:8000/contacts). К шаблонизации в неё отдаётся только переменная `html_map`. Это строка, в которой лежит HTML-код с картой.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
