from taffy.models import *
from django.shortcuts import render
from .serializers import *
from rest_framework.viewsets import ReadOnlyModelViewSet

from rest_flex_fields import is_expanded
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_framework.permissions import IsAuthenticated

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class BloodTypeViewSet(ReadOnlyModelViewSet):
    queryset = BloodType.objects.all()
    serializer_class = BloodTypeSerializer
   

class DaysOfWeekViewSet(ReadOnlyModelViewSet):

    queryset = DaysOfWeek.objects.all()
    serializer_class = DaysOfWeekSerializer
   
class NakSusViewSet(ReadOnlyModelViewSet):

    queryset = NakSus.objects.all()
    serializer_class = NakSusSerializer
   
class RaSiViewSet(ReadOnlyModelViewSet):

    queryset = RaSi.objects.all()
    serializer_class = RaSiSerializer
   


class GenderViewSet(ReadOnlyModelViewSet):

    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
   
class TestesViewSet(ReadOnlyModelViewSet):

    queryset = Testes.objects.all()
    serializer_class = TestesSerializer

class ImageViewSet(FlexFieldsModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
    

class MemberViewSet(FlexFieldsMixin,ReadOnlyModelViewSet):

    # queryset = Member.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MemberSerializer
    permit_list_expands = ['characterneed', 'dayofbirth', 'naksus','testes']
    filterset_fields = ('testes',)


    def get_queryset(self):
        queryset = Member.objects.all()

        if is_expanded(self.request, 'characterneed'):
            queryset = queryset.prefetch_related('characterneed')

        if is_expanded(self.request, 'dayofbirth'):
            queryset = queryset.prefetch_related('dayofbirth')

        # if is_expanded(self.request, 'bloodtype'):
        #     queryset = queryset.prefetch_related('bloodtype')

        if is_expanded(self.request, 'naksus'):
            queryset = queryset.prefetch_related('company')

        if is_expanded(self.request, 'testes'):
            queryset = queryset.prefetch_related('testes')

        return queryset
   
class ConversationViewSet(ReadOnlyModelViewSet):

    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
   
class GoldmemberViewSet(ReadOnlyModelViewSet):

    queryset = Goldmember.objects.all()
    serializer_class = GoldmemberSerializer
    