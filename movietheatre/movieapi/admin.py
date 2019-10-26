from django.contrib import admin
from .models import Movie, Room, Ticket

# Register your models here.

admin.site.register(Movie)
admin.site.register(Room)
admin.site.register(Ticket)
