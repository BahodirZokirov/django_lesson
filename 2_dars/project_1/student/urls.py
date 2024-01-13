from django.urls import path
from .views import *


urlpatterns = [
    path("name/", Name),
    path('age/', Age),
    path('city/', City),
    path('proff/', Proff),
    path('degree/', Degree)
]