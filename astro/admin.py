from django.contrib import admin
from .models import Event, Blog, Profile


# Register your models here.
admin.site.register(Event)
admin.site.register(Blog)
admin.site.register(Profile)
