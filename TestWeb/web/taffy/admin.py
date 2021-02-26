from .models import Match, Message, Profile, Rating

from django.contrib import admin

# Register your models here.
admin.site.register(Profile)
admin.site.register(Rating)
admin.site.register(Match)
admin.site.register(Message)