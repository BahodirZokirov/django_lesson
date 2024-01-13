from django.urls import path
from .views import Name


urlpatterns = [
    path ("name", Name)
]