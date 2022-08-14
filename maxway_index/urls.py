from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('order/', main_order, name="main_order"),
]