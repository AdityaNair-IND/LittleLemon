from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet
from . import views

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('book_table/', views.make_reservation, name='make_reservation'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('reservations/', views.reservation_list, name='reservations_list'),
]
