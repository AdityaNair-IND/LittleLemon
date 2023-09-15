from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('bookings/', include('bookings.urls'),),
    # path('*', )
    # path('.*', include('landingpage.urls')),
    path('landingpage', views.index),
]
