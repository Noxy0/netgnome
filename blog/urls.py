from importlib.resources import path
from django.urls import path

from .views import post_detail, frontpage

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('<slug:slug>/', post_detail, name='post_detail')
]
