from rest_framework import serializers

from .models import Movie, Room, Ticket, BuyTicket


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['name', 'time']


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number', 'size', 'movie']


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ['room']


class BuyTicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuyTicket
        fields = ['date_purchased', 'movie_ticket', 'quantity']
