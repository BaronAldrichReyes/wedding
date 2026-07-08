from django.shortcuts import render

def home(request):
    return render(request, 'guests/rsvp.html') # Or whatever your template file is named!
