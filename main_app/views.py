from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Property:
    def __init__(self, name, address, description, value):
        self.name = name
        self.address = address
        self.description = description
        self.value = value
    
properties = [
    Property('House 1', '3204 Lafayette Ave', 'This house sucks!!', '450,000')
]


def home(request):
    return HttpResponse('<h1>HELLO</h1>')

def about(request):
    return render(request, 'about.html')

def properties_index(request):
    return render(request, 'properties/index.html', {'properties': properties})