from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def view(request):
    return render(request, "viewer.html")
