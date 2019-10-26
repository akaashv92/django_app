from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'setuptickets', views.TicketViewSet)
router.register(r'buyticket', views.BuyTicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]