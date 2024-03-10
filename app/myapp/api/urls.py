from django.urls import path
from .views import *

urlpatterns = [
    path("", ProductApi, name="product"),
]
