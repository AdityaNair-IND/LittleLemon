from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100)
    datetime_string = models.CharField(max_length=19, default='YYYY-MM-DD HH:MM:SS')
    guests = models.PositiveIntegerField()

    def __str__(self):
        return self.name
