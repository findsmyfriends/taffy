from api.models import BloodType, Conversation, DaysOfWeek, Gender, Image, MemberProfile, NakSus, Personality, RaSi, Testes,Handler,Goldmember
from rest_flex_fields import FlexFieldsModelSerializer
from django.contrib.auth.models import User
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_framework import  serializers

class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='product_headshot'
    )

    class Meta:
        model = Image
        fields = ['pk', 'name', 'image']

class BloodTypeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = BloodType
        fields = '__all__'


class DaysOfWeekSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = DaysOfWeek
        fields = '__all__'



class NakSusSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = NakSus
        fields = '__all__'


class RaSiSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = RaSi
        fields = '__all__'

class GenderSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class TestesSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Testes
        fields = '__all__'

class HandlerSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Handler
        fields = '__all__'

class PersonalitySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Personality
        fields = ['pk', 'value']
        # expandable_fields = {
        #     'value': (PersonalitySerializer, {'many': True}),       
        # }

class MemberProfileSerializer(serializers.ModelSerializer):
    # user12 = serializers.StringRelatedField(many=True)

    class Meta:
        model = MemberProfile
        fields = '__all__'
        
        depth = 1
        # fields = ['pk', 'dayofbirth','rasi','age','user12']
        # expandable_fields = {
        #     'user': (UserSerializer, {'username': True}),
            # 'dayofbirth': (DaysOfWeekSerializer, {'many': True}),
            # 'rasi': (RaSiSerializer, {'many': True}),
            # 'bloodtype': (BloodTypeSerializer, {'many': True}),
            # 'naksus': (NakSusSerializer, {'many': True}),
            # 'gender': (GenderSerializer, {'many': True}),
            # 'testes': (TestesSerializer, {'many': True}),
            # 'imageprofile': (ImageSerializer, {'many': True}),
            # 'personality': (PersonalitySerializer, {'many': True}),       
        # }


class ConversationSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'
        expandable_fields = {
          'memberprofile': (MemberProfileSerializer, {'many': True}),
        #   'user': (UserSerializer, {'many': True}),
          'rejected': (HandlerSerializer, {'many': True})
        }

class GoldmemberSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Goldmember
        fields = '__all__'
        expandable_fields = {
          'memberprofile': (MemberProfileSerializer, {'many': True}),
          'Conversation': (ConversationSerializer, {'many': True})
        }

class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['id', 'username','first_name','last_name']
        # expandable_fields = {
        #     'memberprofile': (MemberProfileSerializer, {'many': True}),
        #     'dayofbirth': (DaysOfWeekSerializer, {'many': True}),
        #     'rasi': (RaSiSerializer, {'many': True}),
        #     'bloodtype': (BloodTypeSerializer, {'many': True}),
        #     'naksus': (NakSusSerializer, {'many': True}),
        #     'gender': (GenderSerializer, {'many': True}),
        #     'testes': (TestesSerializer, {'many': True}),
        #     'imageprofile': (ImageSerializer, {'many': True}),
        #     'personality': (PersonalitySerializer, {'many': True}),  
        # }