from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from models import Movie, Showtime, Booking
from forms import MovieForm, ShowtimeForm, BookingForm

# 1. الصفحة الرئيسية
def home(request):
    try:
        movies = Movie.objects.filter(is_showing=True)
        total_m = Movie.objects.count()
        total_b = Booking.objects.count()
    except:
        movies, total_m, total_b = [], 0, 0
    return render(request, 'home.html', {'movies': movies, 'total_movies': total_m, 'total_bookings': total_b})

# 2. الأفلام
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    
    showtimes = Showtime.objects.filter(movie=movie)
    
    return render(request, 'movie_detail.html', {
        'movie': movie,
        'showtimes': showtimes 
    })

def movie_create(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('movie_list')
    return render(request, 'movie_form.html', {'form': form, 'action': 'Add'})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = MovieForm(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movie_list')
    return render(request, 'movie_form.html', {'form': form, 'action': 'Edit'})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'confirm_delete.html', {'object': movie})

# 3. المواعيد (Showtimes) - تأكدي من وجود هذه الدوال
def showtime_list(request):
    showtimes = Showtime.objects.all()
    return render(request, 'showtime_list.html', {'showtimes': showtimes})

def showtime_create(request):
    form = ShowtimeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('showtime_list')
    return render(request, 'showtime_form.html', {'form': form})

def showtime_update(request, pk):
    showtime = get_object_or_404(Showtime, pk=pk)
    form = ShowtimeForm(request.POST or None, instance=showtime)
    if form.is_valid():
        form.save()
        return redirect('showtime_list')
    return render(request, 'showtime_form.html', {'form': form})

def showtime_delete(request, pk):
    showtime = get_object_or_404(Showtime, pk=pk)
    if request.method == 'POST':
        showtime.delete()
        return redirect('showtime_list')
    return render(request, 'confirm_delete.html', {'object': showtime})

# 4. الحجوزات (Booking)
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})

def booking_create(request, showtime_pk):
    # تجيب موعد العرض المحدد بناءً على الـ ID الممرر في الرابط
    showtime = get_object_or_404(Showtime, pk=showtime_pk)
    
    # نجيب الفيلم المرتبط بهذا الموعد تحديداً
    movie = showtime.movie 

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.showtime = showtime  # نربط الحجز بالموعد
            
            # حساب السعر الإجمالي بناءً على سعر الفيلم المختار
            booking.total_price = booking.seats_booked * showtime.price
            booking.status = 'confirmed' 
            
            booking.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    
    # نرسل الـ showtime والـ movie للفورم عشان يعرض الأسماء الصح
    return render(request, 'booking_form.html', {
        'form': form, 
        'showtime': showtime,
        'movie': movie 
    })
# دالة حذف الحجز
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(request, 'confirm_delete.html', {'object': booking})