from rest_framework import routers, serializers
from rest_flex_fields import FlexFieldsModelSerializer
# from rest_framework.validators import UniqueTogetherValidator
from django.utils.timezone import now
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.models import User
from versatileimagefield.serializers import VersatileImageFieldSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# class UserSerializer(FlexFieldsModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# class UserSerializer(FlexFieldsModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username']

# ## -----------------
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



# class PictureURL(models.Model):
#     picpost = models.TextField(blank=True, default="")
#     discription = models.CharField(max_length=1000, default="")
#     created_at = models.DateTimeField(auto_now_add=True)  # When it was create
#     updated_at = models.DateTimeField(auto_now=True)  # When i was update

#     def __str__(self):
#         return f'{self.discription}'


class GenderSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class TestesSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Testes
        fields = '__all__'

class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='product_headshot'
    )

    class Meta:
        model = Image
        fields = ['pk', 'name', 'image']

class MemberSerializer(FlexFieldsModelSerializer):

  
    
    class Meta:
        model = Member
        fields = '__all__'



class ConversationSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'
        expandable_fields = {
          'category': (MemberSerializer, {'many': True})
        }

class GoldmemberSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Goldmember
        fields = '__all__'
        expandable_fields = {
          'category': (MemberSerializer, {'many': True})
        }

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
