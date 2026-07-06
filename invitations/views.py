from django.shortcuts import render

def home(request):
    return render(request, 'index.html') # Or whatever your template file is named!
