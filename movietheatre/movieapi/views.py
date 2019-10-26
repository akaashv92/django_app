from rest_framework import viewsets
from .models import Movie, Room, Ticket, BuyTicket
from .serializers import MovieSerializer, RoomSerializer, TicketSerializer, BuyTicketSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class BuyTicketViewSet(viewsets.ModelViewSet):
    queryset = BuyTicket.objects.all()
    serializer_class = BuyTicketSerializer
