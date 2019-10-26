from django.contrib import admin
from .models import Movie, Room, Ticket, BuyTicket


admin.site.register(Movie)
admin.site.register(Room)
admin.site.register(Ticket)
admin.site.register(BuyTicket)
