from django.contrib.auth.models import User
from api.serializers import *
from api.models import *
from rest_framework import routers, serializers, viewsets  
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_flex_fields import is_expanded
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [IsAuthenticated]

   
class ImageViewSet(FlexFieldsModelViewSet):

    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    # permission_classes = [IsAuthenticated]


class BloodTypeViewSet(viewsets.ModelViewSet):
    queryset = BloodType.objects.all()
    serializer_class = BloodTypeSerializer
    # permission_classes = [IsAuthenticated,]
   

class DaysOfWeekViewSet(viewsets.ModelViewSet):

    queryset = DaysOfWeek.objects.all()
    serializer_class = DaysOfWeekSerializer
    # permission_classes = [IsAuthenticated,]

   
class NakSusViewSet(viewsets.ModelViewSet):

    queryset = NakSus.objects.all()
    serializer_class = NakSusSerializer
    # permission_classes = [IsAuthenticated,]

   
class RaSiViewSet(viewsets.ModelViewSet):

    queryset = RaSi.objects.all()
    serializer_class = RaSiSerializer
    # permission_classes = [IsAuthenticated,]

   

class GenderViewSet(viewsets.ModelViewSet):

    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    # permission_classes = [IsAuthenticated,]

   
class TestesViewSet(viewsets.ModelViewSet):

    queryset = Testes.objects.all()
    serializer_class = TestesSerializer
    # permission_classes = [IsAuthenticated,]

class PersonalityViewSet(viewsets.ModelViewSet):
    queryset = Personality.objects.all()
    serializer_class = PersonalitySerializer

        
class MemberProfileViewSet(viewsets.ModelViewSet):

    queryset = MemberProfile.objects.all()
    serializer_class = MemberProfileSerializer  
    # permission_classes = [AllowAny,]
    filterset_fields = ('testes','personality' )


class HandlerViewSet(viewsets.ModelViewSet):

    queryset = Handler.objects.all()
    serializer_class = HandlerSerializer
    # permission_classes = [IsAuthenticated,]



class ConversationViewSet(viewsets.ModelViewSet):

    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    


class GoldmemberViewSet(viewsets.ModelViewSet):
    queryset = Goldmember.objects.all()
    serializer_class = GoldmemberSerializer


class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
       

def index(req):
    return render(req, 'api/index.html')

