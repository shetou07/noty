from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#this is a function for going home
def home(request):
    return HttpResponse('<h1>Return to base</h1>')