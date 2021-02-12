from django.db.models import fields
from api.models import BloodType, Conversation, DaysOfWeek, Gender, Goldmember, Image, MemberProfile, NakSus, Personality, RaSi, Testes,Handler
from rest_flex_fields import FlexFieldsModelSerializer
from django.contrib.auth.models import User
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_framework import  serializers

class ImageSerializer(FlexFieldsModelSerializer):
    # file_uploaded = serializers.FileField()
    image = VersatileImageFieldSerializer(
        sizes='product_headshot'
    )

    class Meta:
        model = Image
        fields = '__all__'

        # fields = ['id', 'name', 'image']

class BloodTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BloodType
        fields = '__all__'


class DaysOfWeekSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DaysOfWeek
        fields = '__all__'



class NakSusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NakSus
        fields = '__all__'


class RaSiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RaSi
        fields = '__all__'

class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class TestesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Testes
        fields = '__all__'

class HandlerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Handler
        fields = '__all__'

class PersonalitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personality
        fields = ['pk', 'value']
        # expandable_fields = {
        #     'value': (PersonalitySerializer, {'many': True}),       
        # }

class MemberProfileSerializer(FlexFieldsModelSerializer):
    # user12 = serializers.StringRelatedField(many=True)

    class Meta:
        model = MemberProfile   
        fields = '__all__'
        # fields = ['user','birthday','age','rasi','bloodtype','naksus','gender','testes','imageprofile','personality','liked','noped']
        
        # depth = 1



class ConversationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'
        expandable_fields = {
          'memberprofile': (MemberProfileSerializer, {'many': True}),
        #   'user': (UserSerializer, {'many': True}),
          'rejected': (HandlerSerializer, {'many': True})
        }


    

class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GoldmemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goldmember
        fields = '__all__'

        # fields = ['pk', 'dayofbirth','rasi','age','user12']
        expandable_fields = {
            'memberprofile': (MemberProfileSerializer, {'many': True}),
            'conversation': (ConversationSerializer, {'many': True})
            
        }