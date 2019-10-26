from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=60)
    time = models.TimeField()

    def __str__(self):
        return "{} - {}".format(self.name, self.time)


class Room(models.Model):
    room_number = models.IntegerField(max_length=16)
    size = models.IntegerField(max_length=16)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(self.room_number, self.size, self.movie)


class Ticket(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.movie, self.room)
