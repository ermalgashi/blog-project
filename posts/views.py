from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def all_posts(request):
    return HttpResponse("<html><body>It is now.</body></html>")
