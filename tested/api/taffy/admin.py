from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib.auth.models import Group


# Register your models here.
# admin.register() decorator
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
        list_display = ('pk', 'first_name','last_name','age')

admin.site.register(BloodType)
admin.site.register(DaysOfWeek)
admin.site.register(NakSus)
admin.site.register(RaSi)
# admin.site.register(Member)
admin.site.register(Gender)
admin.site.register(Testes)
admin.site.register(Goldmember)
admin.site.register(Conversation)
# admin.site.register(ValuesOfall)
admin.site.register(Image)
admin.site.unregister(Group)

admin.site.site_header = "Members Taffy Admin"
