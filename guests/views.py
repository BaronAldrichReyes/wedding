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
            
            # Instead of redirect, we re-render the page with an empty form
            return render(request, 'guests/rsvp.html', {'form': RSVPForm()})
    
    return render(request, 'guests/rsvp.html', {'form': RSVPForm()})

def find_seat(request):
    query = request.GET.get('name')
    
    if query:
        clean_query = query.strip()
        parts = clean_query.split()
        
        if len(parts) == 1:
            word = parts[0]
            guests = Guest.objects.filter(
                Q(first_name__istartswith=word) | Q(last_name__istartswith=word)
            )
        else:
            first_part = parts[0]
            last_part = parts[1]
            guests = Guest.objects.filter(
                Q(first_name__istartswith=first_part) & Q(last_name__istartswith=last_part)
            )
        
        # This line must be aligned with `if len(parts) == 1:`
        return render(request, 'guests/seat_result.html', {'guests': guests, 'query': query})
        
    return render(request, 'guests/seat_result.html')