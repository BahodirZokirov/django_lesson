from django.contrib import admin

# Register your models here.


from .models import Teachers
from .models import Rocks


admin.site.register(Teachers)
admin.site.register(Rocks)