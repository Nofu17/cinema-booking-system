from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in minutes")
    description = models.TextField()
    rating = models.FloatField()
    # هنا التاريخ يكون سنة
    release_date = models.IntegerField(help_text="Release Year (e.g. 2014)")
    is_showing = models.BooleanField(default=True)

    class Meta:
        app_label = 'auth'

    def __str__(self):
        return self.title

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall_name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available_seats = models.IntegerField()

    class Meta:
        app_label = 'auth'

    def __str__(self):
        return f"{self.movie.title} - {self.hall_name}"

class Booking(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField(null=True, blank=True)
    seats_booked = models.IntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    
    status = models.CharField(max_length=20, default='confirmed') 

    class Meta:
        app_label = 'auth'

    def __str__(self):
        return f"{self.customer_name} - {self.showtime.movie.title}"