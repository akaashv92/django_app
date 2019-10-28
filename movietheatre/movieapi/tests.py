import datetime

from django.test import TestCase, Client

from .models import Room, Movie, Ticket, BuyTicket


# Testing the Movie Model
class MovieTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(name='Titanic', time='08:00:00')
        Movie.objects.create(name='Avengers', time='10:00:00')

    def test_movies_exist(self):
        titanic = Movie.objects.get(name='Titanic')
        self.assertEquals(titanic.name, 'Titanic')
        self.assertEquals(titanic.time, datetime.time(8, 0))

        avengers = Movie.objects.get(name='Avengers')
        self.assertEquals(avengers.name, 'Avengers')
        self.assertEquals(avengers.time, datetime.time(10, 0))


# Testing the Room Model
class RoomTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(name='Batman', time=datetime.time(8, 0))
        Movie.objects.create(name='Joker', time=datetime.time(10, 0))
        batman = Movie.objects.get(name='Batman')
        joker = Movie.objects.get(name='Joker')

        Room.objects.create(room_number=1, size=10, movie=batman)
        Room.objects.create(room_number=2, size=20, movie=joker)

    def test_room_exist(self):
        batman = Movie.objects.get(name='Batman')
        joker = Movie.objects.get(name='Joker')

        room_one = Room.objects.get(room_number=1)
        self.assertEquals(room_one.room_number, 1)
        self.assertEquals(room_one.size, 10)
        self.assertEquals(room_one.movie, batman)

        room_two = Room.objects.get(room_number=2)
        self.assertEquals(room_two.room_number, 2)
        self.assertEquals(room_two.size, 20)
        self.assertEquals(room_two.movie, joker)


class TicketTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(name='Batman', time=datetime.time(8, 0))
        batman = Movie.objects.get(name='Batman')
        Room.objects.create(room_number=1, size=10, movie=batman)
        room_one = Room.objects.get(room_number=1)
        Ticket.objects.create(room=room_one)

    def test_ticket_exist(self):
        room_one = Room.objects.get(room_number=1)
        ticket = Ticket.objects.get(room=room_one)
        self.assertEquals(ticket.room, room_one)


class BuyTicketTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(name='Batman', time=datetime.time(8, 0))
        batman = Movie.objects.get(name='Batman')
        Room.objects.create(room_number=1, size=10, movie=batman)
        room_one = Room.objects.get(room_number=1)
        Ticket.objects.create(room=room_one)
        ticket = Ticket.objects.get(room=1)
        BuyTicket.objects.create(date_purchased=datetime.time(4, 0), movie_ticket=ticket)

    def test_bought_ticket_exists(self):
        ticket = Ticket.objects.get(room=1)
        buy_ticket = BuyTicket.objects.get(movie_ticket=ticket)
        self.assertEquals(buy_ticket.movie_ticket, ticket)


# Testing views
class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    # Testing Movie Views
    def test_movie_index(self):
        response = self.client.get('/movies/')
        self.assertEquals(response.status_code, 200)

    def test_movie_with_no_content(self):
        response = self.client.get('/movies/12345/')
        self.assertEquals(response.status_code, 404)

    def test_movie_exists(self):
        Movie.objects.create(name='Joker', time=datetime.time(6, 0))
        response = self.client.get('/movies/1/')
        self.assertEquals(response.status_code, 200)

    # Testing Room Views
    def test_room_index(self):
        response = self.client.get('/rooms/')
        self.assertEquals(response.status_code, 200)

    def test_invalid_room(self):
        response = self.client.get('/movies/12345/')
        self.assertEquals(response.status_code, 404)

    def test_room_details(self):
        Movie.objects.create(name='Joker', time=datetime.time(6, 0))
        joker = Movie.objects.get(name='Joker')
        Room.objects.create(room_number=1, size=10, movie=joker)
        response = self.client.get('/rooms/1/')
        self.assertEquals(response.status_code, 200)

    # Testing the Tickets View
    def test_ticket_index(self):
        response = self.client.get('/setuptickets/')
        self.assertEquals(response.status_code, 200)

    def test_invalid_ticket(self):
        response = self.client.get('/setuptickets/12345/')
        self.assertEquals(response.status_code, 404)

    def test_get_ticket(self):
        Movie.objects.create(name='Joker', time=datetime.time(6, 0))
        joker = Movie.objects.get(name='Joker')
        Room.objects.create(room_number=1, size=10, movie=joker)
        room_one = Room.objects.get(room_number=1)
        Ticket.objects.create(room=room_one)
        response = self.client.get('/setuptickets/1/')
        self.assertEquals(response.status_code, 200)


# Testing JSON
class JSONTestCase(TestCase):

    def test_get_empty_movies(self):
        response = self.client.get('/movies/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(str(response.content, encoding='utf8'), '[]')

    def test_get_added_movies(self):
        Movie.objects.create(name='Joker', time=datetime.time(6, 0))
        response = self.client.get('/movies/1/')
        self.assertEquals(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {"name": "Joker",
                                                                      "time": "06:00:00"})

    def test_get_rooms(self):
        Movie.objects.create(name='Joker', time=datetime.time(6, 0))
        joker = Movie.objects.get(name='Joker')
        Room.objects.create(room_number=1, size=10, movie=joker)
        response = self.client.get('/rooms/1/')
        self.assertEquals(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),
                             {"room_number": 1, "size": 10, "movie": "http://testserver/movies/1/"})
