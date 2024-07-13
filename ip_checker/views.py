from django.shortcuts import render


def index(request):
    return render(request, 'ip_checker.html')

# Create your views here.
