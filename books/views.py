from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random

def current_time(request):
    now = datetime.now().strftime("%H:%M:%S")
    return HttpResponse(f"<h1>Текущее время: {now}</h1>")

def random_number(request):
    number = random.randint(1, 100)
    return HttpResponse(f"<h1>Случайное число: {number}</h1>")

def about_me(request):
    return HttpResponse("<h1>Я</h1><p>Чынгызхан</p>")

