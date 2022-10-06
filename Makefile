build:
	@docker build . && docker-compose build

up:
	@docker-compose up

down:
	@docker-compose down

superuser:
	@docker-compose run --rm django-app sh -c "python3 manage.py createsuperuser"

create-app:
	@docker-compose run --rm django-app sh -c "django-admin startapp $(NAME)"

migrations:
	@docker-compose run --rm django-app sh -c "python manage.py makemigrations"

migrate-init:
	@docker-compose run --rm django-app sh -c "python manage.py migrate --fake-initial"

migrate:
	@docker-compose run --rm django-app sh -c "python manage.py migrate"

migrate-init:
	@docker-compose run --rm django-app sh -c "python manage.py migrate --fake-initial"

test:
	@docker-compose run --rm django-app sh -c "python manage.py test"

lint:
	@docker-compose run --rm django-app sh -c "flake8"