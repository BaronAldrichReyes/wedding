from django.contrib import admin
from django.urls import path

# Import the views from both apps with clear, distinct nicknames
from invitations import views as invitation_views
from guests import views as guest_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Your Main One-Page Wedding Site (Root URL)
    # This loads the home view from your invitations app immediately
    path('', invitation_views.home, name='wedding_home'),
    
    # 2. Your RSVP Form Submission Endpoint
    # When someone clicks "Submit" on your one-page form, it sends the data here
    path('rsvp/submit/', guest_views.rsvp_page, name='rsvp_submit'),
]
