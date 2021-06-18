from django.contrib import admin
from .models import Fruit, Provider, Bundle

# Register your models here.

admin.site.register(Fruit)
admin.site.register(Provider)
admin.site.register(Bundle)