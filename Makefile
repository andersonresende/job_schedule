run:
	python manage.py runserver

ubuntu:
	ssh -i ~/Downloads/tangerinalab.pem ubuntu@ec2-54-232-20-254.sa-east-1.compute.amazonaws.com

migrate:
	python manage.py makemigrations business
	python manage.py migrate business
	python manage.py migrate

delete_db:
	rm db*
	rm -rf business/migrations/

user:
	python manage.py createsuperuser --username root --email r@r.com

db: delete_db migrate user
