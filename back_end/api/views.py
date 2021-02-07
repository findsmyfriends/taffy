from django.contrib.auth.models import User
from api.serializers import BloodTypeSerializer, ConversationSerializer, DaysOfWeekSerializer, GenderSerializer, GoldmemberSerializer, HandlerSerializer,  ImageSerializer, MemberProfileSerializer, NakSusSerializer, PersonalitySerializer, RaSiSerializer, TestesSerializer,UserSerializer
from api.models import BloodType, Conversation, DaysOfWeek, Gender, Goldmember, Image, MemberProfile, NakSus, Personality, RaSi, Testes,Handler
from rest_framework import routers, serializers, viewsets  
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_flex_fields import is_expanded
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import generics, mixins, permissions
# Create your views here.

class UserViewSet(FlexFieldsModelViewSet,ReadOnlyModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [IsAuthenticated]

   
class ImageViewSet(FlexFieldsModelViewSet):

    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    # permission_classes = [IsAuthenticated]


class BloodTypeViewSet(FlexFieldsModelViewSet,ReadOnlyModelViewSet):
    queryset = BloodType.objects.all()
    serializer_class = BloodTypeSerializer
    # permission_classes = [IsAuthenticated,]
   

class DaysOfWeekViewSet(FlexFieldsModelViewSet,ReadOnlyModelViewSet):

    queryset = DaysOfWeek.objects.all()
    serializer_class = DaysOfWeekSerializer
    # permission_classes = [IsAuthenticated,]

   
class NakSusViewSet(FlexFieldsModelViewSet,ReadOnlyModelViewSet):

    queryset = NakSus.objects.all()
    serializer_class = NakSusSerializer
    # permission_classes = [IsAuthenticated,]

   
class RaSiViewSet(FlexFieldsModelViewSet,ReadOnlyModelViewSet):

    queryset = RaSi.objects.all()
    serializer_class = RaSiSerializer
    # permission_classes = [IsAuthenticated,]

   

class GenderViewSet(FlexFieldsModelViewSet,ReadOnlyModelViewSet):

    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    # permission_classes = [IsAuthenticated,]

   
class TestesViewSet(FlexFieldsModelViewSet,ReadOnlyModelViewSet):

    queryset = Testes.objects.all()
    serializer_class = TestesSerializer
    # permission_classes = [IsAuthenticated,]

class PersonalityViewSet(FlexFieldsModelViewSet,ReadOnlyModelViewSet):
    queryset = Personality.objects.all()
    serializer_class = PersonalitySerializer

        
class MemberProfileViewSet(FlexFieldsModelViewSet,ReadOnlyModelViewSet):

    queryset = MemberProfile.objects.all()
    serializer_class = MemberProfileSerializer  
    # permission_classes = [AllowAny,]


class HandlerViewSet(FlexFieldsModelViewSet,ReadOnlyModelViewSet):

    queryset = Handler.objects.all()
    serializer_class = HandlerSerializer
    # permission_classes = [IsAuthenticated,]



class ConversationViewSet(FlexFieldsModelViewSet,ReadOnlyModelViewSet):

    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    # permission_classes = [IsAuthenticated,]


    # permission_classes = [IsAuthenticated,]


class GoldmemberViewSet(viewsets.ModelViewSet):
    # queryset = Goldmember.objects.all()
    serializer_class = GoldmemberSerializer
       
    # permission_classes = [IsAuthenticated]
    # serializer_class = MemberProfileSerializer
    permit_list_expands = [
            'memberprofile',
            'conversation',
            'memberprofile.user',
            'memberprofile.dayofbirth',
            'memberprofile.rasi',
            'memberprofile.naksus',
            'memberprofile.bloodtype',
            'memberprofile.gender',
            'memberprofile.testes',
            'memberprofile.personality',

            ]

    # filterset_fields = ('memberprofile.testes','memberprofile.personality' )


    def get_queryset(self):
        queryset = Goldmember.objects.all()

        if is_expanded(self.request, 'memberprofile'):
            queryset = queryset.prefetch_related('memberprofile')

        if is_expanded(self.request, 'conversation'):
            queryset = queryset.prefetch_related('conversation')

        if is_expanded(self.request, 'user'):
            queryset = queryset.prefetch_related('memberprofile__user')

        if is_expanded(self.request, 'dayofbirth'):
            queryset = queryset.prefetch_related('memberprofile__dayofbirth')

        if is_expanded(self.request, 'rasi'):
            queryset = queryset.prefetch_related('memberprofile__rasi')

        if is_expanded(self.request, 'naksus'):
            queryset = queryset.prefetch_related('memberprofile__naksus')

        if is_expanded(self.request, 'gender'):
            queryset = queryset.prefetch_related('memberprofile__gender')

        if is_expanded(self.request, 'testes'):
            queryset = queryset.prefetch_related('memberprofile__testes')

        if is_expanded(self.request, 'imageprofile'):
            queryset = queryset.prefetch_related('imageprofile')

        if is_expanded(self.request, 'personality'):
            queryset = queryset.prefetch_related('memberprofile__personality')

        return queryset

class MemberIsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


   