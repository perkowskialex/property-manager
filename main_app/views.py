from django.shortcuts import render
from django.http import HttpResponse
from .models import Property

# Create your views here.

def home(request):
    return HttpResponse('<h1>HELLO</h1>')

def about(request):
    return render(request, 'about.html')

def properties_index(request):
    properties = Property.objects.all()
    return render(request, 'properties/index.html', {'properties': properties})

def properties_detail(request, p_id):
    p = Property.objects.get(id = p_id)
    return render(request, 'properties/detail.html', {'p': p})