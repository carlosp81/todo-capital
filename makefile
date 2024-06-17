PORT = port
SOURCE = s
DESTINATION = d

django-project:
		poetry run django-admin startproject config src/

server:
		poetry run python src/manage.py runserver $(port)

make-migrations:
		poetry run python src/manage.py makemigrations

migrate:
		poetry run python src/manage.py migrate

add-super:
		poetry run python src/manage.py createsuperuser

startap:
		mkdir -p ${d}
		poetry run python src/manage.py startapp ${s} ${d}


.PHONY: django-project server make-migrations migrate add-super startapp
