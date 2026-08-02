from django.contrib import admin
from django.urls import path
from guests import views

# Import the views from both apps with clear, distinct nicknames
from invitations import views as invitation_views
from guests import views as guest_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', invitation_views.home, name='wedding_home'),
    path('rsvp/submit/', guest_views.rsvp_page, name='rsvp_submit'),
    path('find-seat/', views.find_seat, name='find_seat'),
]
