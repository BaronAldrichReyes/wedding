from django.shortcuts import render

def home(request):
    return render(request, 'rsvp.html') # Or whatever your template file is named!
