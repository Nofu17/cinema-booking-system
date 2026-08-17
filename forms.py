from django import forms
from models import Movie, Showtime, Booking

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'duration', 'description', 'release_date', 'rating', 'is_showing']

class ShowtimeForm(forms.ModelForm):
    class Meta:
        model = Showtime
        fields = ['movie', 'start_time', 'hall_name', 'price', 'available_seats']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'seats_booked']