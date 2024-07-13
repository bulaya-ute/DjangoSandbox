from django.shortcuts import render
from django.http import HttpResponse
import requests


def check_device_status(ip):
    try:
        response = requests.get(f'http://{ip}')
        if 'specific message' in response.text:
            return True
    except requests.RequestException:
        return False
    return False


def active_devices(request):
    ip_addresses = [
        "192.168.1.1",
        "192.168.1.2",
        "192.168.1.3",
        # Add more IP addresses here
    ]

    active_devices = [ip for ip in ip_addresses if check_device_status(ip)]

    context = {
        'active_devices': active_devices
    }
    return render(request, 'checker/active_devices.html', context)


# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")
