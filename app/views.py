from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(request):
    return HttpResponse('<h1>Good Morning</h1>')