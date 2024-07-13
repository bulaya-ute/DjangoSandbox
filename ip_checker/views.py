from django.http import HttpResponse
from django.shortcuts import render
import requests


def check_device_status(ip):
    return True
    try:
        response = requests.get(f'http://{ip}')
        if 'specific message' in response.text:
            return True
    except requests.RequestException:
        return False
    return False


def index(request):
    ip_addresses = [
        "192.168.1.1:5000",
        "192.168.1.2:5000",
        "192.168.1.3:5000",
        # Add more IP addresses here
    ]

    active_devices = [ip for ip in ip_addresses if check_device_status(ip)]

    context = {
        'active_devices': active_devices
    }
    return render(request, 'ip_checker/index.html', context)


def handle_prefix(request, anything):
    return HttpResponse(f'You requested the URL: {anything}')
