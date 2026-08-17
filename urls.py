from django.contrib import admin
from django.urls import path
import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # الأفلام - الأساسيات فقط
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movies/add/', views.movie_create, name='movie_create'),
    path('movies/<int:pk>/edit/', views.movie_update, name='movie_update'),
    path('movies/<int:pk>/delete/', views.movie_delete, name='movie_delete'),
    
    # المواعيد - الأساسيات فقط
    path('showtimes/', views.showtime_list, name='showtime_list'),
    path('showtimes/add/', views.showtime_create, name='showtime_create'),
    path('showtimes/<int:pk>/edit/', views.showtime_update, name='showtime_update'),
    path('showtimes/<int:pk>/delete/', views.showtime_delete, name='showtime_delete'),
    
    # الحجوزات
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/add/<int:showtime_pk>/', views.booking_create, name='booking_create'),
    path('bookings/<int:pk>/delete/', views.booking_delete, name='booking_delete'),
]