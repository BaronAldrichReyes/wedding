from django.shortcuts import render, redirect
from django.contrib import messages  # <-- Imports the pop-up tool
from .forms import RSVPForm
from django.db.models import Q
from .models import Guest

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
        guest = Guest.objects.filter(Q(name__icontains=query)).first()
        return render(request, 'guests/seat_result.html', {'guest': guest, 'query': query})

    return render(request, 'guests/search_form.html')