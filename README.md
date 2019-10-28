# DJANGO Rest Framework

This is a Movie Theatre API.

An Admin can: 
1) Add Movies
2) Set up Rooms with movies and time
3) Sell Tickets

A Customer can:
1) See the list of movies screened and time of the show
2) See the list of Rooms with movies
3) Buy a ticket

Packages used Django rest framework

Db used SQLite

Runs on http://localhost:8000/

Admin page http://localhost:8000/admin

username: movieAdmin
password: movietheatre

You can add/delete movies, rooms and tickets from the API and from the admin page.

Make sure to have the database tables created before running the tests

`python manage.py makemigrations`

`python manage.py test`



