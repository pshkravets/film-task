from django.contrib import admin
from .models import Moovie, Actor, Producer


admin.site.register(Actor)
admin.site.register(Producer)
admin.site.register(Moovie)