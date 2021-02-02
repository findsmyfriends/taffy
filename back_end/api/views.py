from api.models import *
from api.serializers import *
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_flex_fields import is_expanded
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserViewSet(FlexFieldsModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

   
class ImageViewSet(FlexFieldsModelViewSet):

    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    # permission_classes = [IsAuth  enticated]


class BloodTypeViewSet(FlexFieldsModelViewSet,ReadOnlyModelViewSet):
    queryset = BloodType.objects.all()
    serializer_class = BloodTypeSerializer
    # permission_classes = [IsAuthenticated,]
   

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

class MemberProfileViewSet(FlexFieldsModelViewSet):

    queryset = MemberProfile.objects.all()
    serializer_class = MemberProfileSerializer

        # queryset = Member.objects.all()
    # permission_classes = [IsAuthenticated]
    # serializer_class = MemberProfileSerializer
    # permit_list_expands = ['user',
    #         'dayofbirth',
    #         'dayofbirth.daysofweek',
    #         'rasi',
    #         'bloodtype',
    #         'naksus',
    #         'gender',
    #         'testes',
    #         'imageprofile',
    #         'personality', 
    #         'personality.value', 

    #         ]

    # filterset_fields = ('testes','personality' )


    # def get_queryset(self):
    #     queryset = MemberProfile.objects.all()

    #     if is_expanded(self.request, 'user'):
    #         queryset = queryset.prefetch_related('user')

    #     if is_expanded(self.request, 'dayofbirth'):
    #         queryset = queryset.prefetch_related('dayofbirth')

    #     if is_expanded(self.request, 'daysofweek'):
    #         queryset = queryset.prefetch_related('dayofbirth__daysofweek')

    #     if is_expanded(self.request, 'rasi'):
    #         queryset = queryset.prefetch_related('rasi')

    #     if is_expanded(self.request, 'bloodtype'):
    #         queryset = queryset.prefetch_related('bloodtype')

    #     if is_expanded(self.request, 'naksus'):
    #         queryset = queryset.prefetch_related('naksus')

    #     if is_expanded(self.request, 'gender'):
    #         queryset = queryset.prefetch_related('gender')

    #     if is_expanded(self.request, 'testes'):
    #         queryset = queryset.prefetch_related('testes')

    #     if is_expanded(self.request, 'imageprofile'):
    #         queryset = queryset.prefetch_related('imageprofile')

    #     if is_expanded(self.request, 'personality'):
    #         queryset = queryset.prefetch_related('personality')

    #     if is_expanded(self.request, 'value'):
    #         queryset = queryset.prefetch_related('personality__value')


    #     return queryset