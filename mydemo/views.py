# Create your views here.
from django.shortcuts import render


def index(request):
    return render("demo")


def tell_me(request):
    return render("demo")