from django.contrib import admin
from .models import Booking, Showtime, Movie

admin.site.register(Booking)
admin.site.register(Showtime)
admin.site.register(Movie)