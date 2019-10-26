from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer, RoomSerializer, TicketSerializer
from .models import Movie, Room, Ticket


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
