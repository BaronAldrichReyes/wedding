from django.shortcuts import render, redirect
from django.contrib import messages  # <-- Imports the pop-up tool
from .forms import RSVPForm
from django.db.models import Q
from .models import Guest
from django.db.models import Value
from django.db.models.functions import Concat

def rsvp_page(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            guest = form.save()
            if guest.is_attending:
                messages.success(request, f"Thank you, {guest.first_name}! See you there! 🎉")
            else:
                messages.info(request, f"Thank you, {guest.first_name}. We'll miss you!")
            return render(request, 'guests/rsvp.html', {'form': RSVPForm()})
    
    return render(request, 'guests/rsvp.html', {'form': RSVPForm()})

def find_seat(request):
    query = request.GET.get('name')
    
    if query:
        words = query.split()
        guests = Guest.objects.all()
        for word in words:
            guests = guests.filter(
                Q(first_name__icontains=word) | Q(last_name__icontains=word)
            )
        
        return render(request, 'guests/seat_result.html', {'guests': guests, 'query': query})
        
    return render(request, 'guests/seat_result.html')