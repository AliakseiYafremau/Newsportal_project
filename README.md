# Новостной портал
## О проекте
Сайт дает возможность добавлять новости, изменять, а также удалять. Сайт поддерживает аутентификацию, имеет русскую версию и английскую.
## Запуск
Для начала клонируйте репозиторий
```bash
git clone https://github.com/AliakseiYafremau/Newsportal_project
```
Перейдите в корневую папку проекта и создайте виртуальное окружение
```bash
python -m venv venv
```
Активируйте виртуальное окружение
1. Активация на Windnows
```bash
venv/Scripts/activate
```
2. Активация на Linux
```bash
source venv/bin/activate
```
Скачайте все необходимые библиотеки
```bash
pip install -r requirements.txt
```
Запустите проект через
```bash
python manage.py runserver
```