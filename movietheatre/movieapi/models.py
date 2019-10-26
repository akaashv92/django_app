from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=60, help_text="Name of the movie")
    time = models.TimeField(help_text="Show Timing")

    def __str__(self):
        return "{} - {}".format(self.name, self.time)


class Room(models.Model):
    room_number = models.IntegerField(max_length=16, help_text="Room Number")
    size = models.IntegerField(max_length=16, help_text="Seating Capacity")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, help_text="Movie screened in the room")

    def __str__(self):
        return "Room:{} - Movie:{}".format(self.room_number, self.movie)


class Ticket(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, help_text="Tickets to Sell")

    def __str__(self):
        return "{}".format(self.room)


class BuyTicket(models.Model):
    date_purchased = models.DateField(auto_now_add=True)
    movie_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, help_text="Ticket to buy")

    def __str__(self):
        return "{} - {}".format(self.date_purchased, self.movie_ticket)
