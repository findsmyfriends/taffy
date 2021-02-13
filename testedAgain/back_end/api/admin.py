from api.serializers import MemberProfileSerializer
from django.conf import settings
from api.models import *
from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
admin.site.unregister(Group)

admin.site.site_header = "APIs For FlutterApp Admin."
# @admin.register(settings.AUTH_USER_MODEL,Member)
@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
        list_display = ('id','gender','testes','age')
# admin.site.register(MemberProfile)
admin.site.register(BloodType)
admin.site.register(DaysOfWeek)
admin.site.register(NakSus)
admin.site.register(RaSi)
admin.site.register(Personality)
admin.site.register(Image)
admin.site.register(Gender)
admin.site.register(Testes)
admin.site.register(Handler)
admin.site.register(Goldmember)
admin.site.register(Conversation)


