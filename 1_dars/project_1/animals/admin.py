from django.contrib import admin

# Register your models here.



from .models import Animal
from .models import Students



admin.site.register (Animal)
admin.site.register (Students)

