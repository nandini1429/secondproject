from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def good_morning_view(request):
    msg = "<h1>Hello Friend Good Morning!!!</h1>"
    return HttpResponse(msg)

def good_afternoon_view(request):
    msg = "<h1>Hello Friend Good Afternoon!!!</h1>"
    return HttpResponse(msg)

def good_evening_view(request):
    msg = "<h1>Hello Friend Good Evening!!! and welcome to gitub commit</h1>"
    return HttpResponse(msg)
