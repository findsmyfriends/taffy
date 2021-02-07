from django.conf import settings
from api.models import BloodType, Conversation, DaysOfWeek, Gender, Goldmember, Handler, Image, LikedManager, MemberProfile, MemberProfile, NakSus, NopedManager, Personality, RaSi, Testes
from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
admin.site.unregister(Group)

admin.site.site_header = "APIs For FlutterApp Admin."
# @admin.register(settings.AUTH_USER_MODEL,MemberProfile)
@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
        list_display = ('id','user','first_name','last_name','gender','testes','age')

admin.site.register(BloodType)
admin.site.register(DaysOfWeek)
admin.site.register(NakSus)
admin.site.register(RaSi)
admin.site.register(Handler)
admin.site.register(Gender)
admin.site.register(Testes)
admin.site.register(Goldmember)
admin.site.register(Conversation)
admin.site.register(Personality)
admin.site.register(Image)
