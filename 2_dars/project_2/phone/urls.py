from django.urls import path
from .views import *


urlpatterns = [
    path('iphone/', Iphone),
    path('samsung/', Samsung),
    path('mi/', Mi)
]