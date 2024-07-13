from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ip_checker'),
    path('<path:anything>/', views.handle_prefix, name='handle_prefix'),
]
