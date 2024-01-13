from django.urls import path
from .views import *


urlpatterns = [
    path('lenovo/', Lenovo),
    path('hp/', Hp),
    path('asus/', Asus)
]