from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets
from .models import *
from .serializers import *

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class BloodTypeViewSet(viewsets.ModelViewSet):
    queryset = BloodType.objects.all()
    serializer_class = BloodTypeSerializer


class DaysOfWeekViewSet(viewsets.ModelViewSet):

    queryset = DaysOfWeek.objects.all()
    serializer_class = DaysOfWeekSerializer


class NakSusViewSet(viewsets.ModelViewSet):

    queryset = NakSus.objects.all()
    serializer_class = NakSusSerializer


class RaSiViewSet(viewsets.ModelViewSet):

    queryset = RaSi.objects.all()
    serializer_class = RaSiSerializer


# class PictureURL(models.Model):
#     picpost = models.TextField(blank=True, default="")
#     discription = models.CharField(max_length=1000, default="")
#     created_at = models.DateTimeField(auto_now_add=True)  # When it was create
#     updated_at = models.DateTimeField(auto_now=True)  # When i was update

#     def __str__(self):
#         return f'{self.discription}'


class GenderViewSet(viewsets.ModelViewSet):

    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class TestesViewSet(viewsets.ModelViewSet):

    queryset = Testes.objects.all()
    serializer_class = TestesSerializer


class MemberViewSet(viewsets.ModelViewSet):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class ConversationViewSet(viewsets.ModelViewSet):

    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class GoldmemberViewSet(viewsets.ModelViewSet):

    queryset = Goldmember.objects.all()
    serializer_class = GoldmemberSerializer
### -----------------
# Routers provide an easy way of automatically determining the URL conf.
# router.register(r'users', UserViewSet)
router = routers.DefaultRouter()

router.register(r'bloodtype', BloodTypeViewSet)
router.register(r'daysofweek', DaysOfWeekViewSet)
router.register(r'naksus', NakSusViewSet)
router.register(r'rasi', RaSiViewSet)
router.register(r'gender', GenderViewSet)
router.register(r'testes', TestesViewSet)
router.register(r'member', MemberViewSet)
router.register(r'conversation', ConversationViewSet)
router.register(r'goldmember', GoldmemberViewSet)
# Create your views here.
def index(req):
    return render(req, 'api/index.html')