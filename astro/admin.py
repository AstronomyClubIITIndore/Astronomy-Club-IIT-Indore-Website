from django.contrib import admin
from .models import Event, Blog, Profile,AllowedPerson,Interview,Photo, Publication


# Register your models here.
admin.site.register(Event)
admin.site.register(Blog)
admin.site.register(Profile)
admin.site.register(AllowedPerson)
admin.site.register(Interview)
admin.site.register(Photo)
admin.site.register(Publication)
