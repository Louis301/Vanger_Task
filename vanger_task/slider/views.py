# slider/views.py
from django.shortcuts import render
from .models import SliderImage

def index(request):
    """Главная страница со слайдером"""
    images = SliderImage.objects.filter(is_active=True).order_by('order')
    return render(request, 'slider/index.html', {'images': images})