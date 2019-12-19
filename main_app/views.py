from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>HELLO</h1>')

def about(request):
    return render(request, 'about.html')

def properties_index(request):
    return render(request, 'properties/index.html', {'properties': properties})