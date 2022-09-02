
from django.shortcuts import render
from django.http import request
from django.contrib import admin

# Create your views here.

def homepage(request):
    return render(request, 'base.html')

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
