from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.db import models
from .models import Booking
from .serializers import BookingSerializer
from .forms import BookingForm
import datetime


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def confirmation(request):
    try:
        print(request.GET)
        extra_guests = request.GET.get('extra_guests')
        extra_charge = request.GET.get('extra_charge')
        return render(request, 'bookings/confirmation.html', {'extra_guests': extra_guests, 'extra_charge': extra_charge})
    except Exception as e:
        print(e)
        return render(request, 'bookings/booking.html',)

def make_reservation(request):
    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    max_datetime = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save it to the database
            booking = form.save()

            # Implement the logic to check the total number of guests here
            total_guests = Booking.objects.filter(datetime=booking.datetime).aggregate(total_guests=models.Sum('guests'))['total_guests']
            max_guest_limit = 50

            if total_guests and total_guests > max_guest_limit:
                extra_guests = total_guests - max_guest_limit
                extra_charge = extra_guests * 150
                
                return render(request, 'bookings/confirmation.html', {'extra_guests': extra_guests, 'extra_charge': extra_charge})

            # Redirect to the confirmation page
            return redirect('bookings:confirmation')
    else:
        form = BookingForm()

    return render(request, 'bookings/booking.html', {'form': form, 'current_datetime': current_datetime, 'max_datetime': max_datetime})

def reservation_list(request):
    reservations = Booking.objects.all()

    return render(request, 'bookings/reservation.html', {'reservations': reservations})
