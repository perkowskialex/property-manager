from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('properties/', views.properties_index, name = 'index'),
    path('properties/<int:p_id>/', views.properties_detail, name = 'detail')
]