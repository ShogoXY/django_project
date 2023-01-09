from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world from Django")
# Create your views here.
