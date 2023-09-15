from django.contrib import admin
from django.urls import path, include
from landingpage import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookings/', include('bookings.urls')),
    path('', views.index), 
]