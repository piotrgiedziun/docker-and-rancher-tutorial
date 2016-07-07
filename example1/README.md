# Sample Project - example #1

## TODO

    - build docker-compose
    - run docker-compose containers
    - update the h1 content in web/demo/views.py
    - update docker-compose config to mount volume
    - update the h1 content in web/demo/views.py

    [advanced]
    - migrate database
    - update the Pizza model (demo/models.py)
    - make migrations & update database
    - display name of pizza in the database (Pizza.objects.get())

## HELP

    - make migrations
    docker-compose run --rm web python manage.py makemigrations demo

    - sync model
    docker-compose run --rm web python manage.py migrate
