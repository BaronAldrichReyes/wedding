from django.contrib import admin
from django.urls import path
from wedding import views  # Replace 'your_app_name' with your actual app name (e.g., 'rsvp', 'wedding')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This empty '' means: "Load this view on the absolute front page"
    path('', views.home, name='home'), 
]
