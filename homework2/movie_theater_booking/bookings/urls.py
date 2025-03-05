from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, home, movie_list, seats, booking_history
from django.urls import path
from . import views


router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
    path('movie-list/', movie_list, name='movie-list'),
    path('seat-booking/', seats, name='seat-booking'),
    path('booking-history/', booking_history, name='booking-history'),
]
