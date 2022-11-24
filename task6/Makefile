DC = docker-compose
APACHE_CONTAINER = django-apache

up:
	$(DC) up

stop:
	$(DC) stop

reload:
	$(DC) kill -s "USR1" $(APACHE_CONTAINER)