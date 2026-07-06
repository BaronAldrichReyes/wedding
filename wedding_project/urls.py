from django.contrib import admin
from django.urls import path
from guests import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rsvp/', views.rsvp_page, name='rsvp'),
]