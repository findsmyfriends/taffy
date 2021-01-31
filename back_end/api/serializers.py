from rest_framework import routers, serializers, viewsets
from rest_framework.validators import UniqueTogetherValidator
from .models import *
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']



# ## -----------------
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



# class PictureURL(models.Model):
#     picpost = models.TextField(blank=True, default="")
#     discription = models.CharField(max_length=1000, default="")
#     created_at = models.DateTimeField(auto_now_add=True)  # When it was create
#     updated_at = models.DateTimeField(auto_now=True)  # When i was update

#     def __str__(self):
#         return f'{self.discription}'


class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class TestesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Testes
        fields = '__all__'


class MemberSerializer(serializers.HyperlinkedModelSerializer):

  
    
    class Meta:
        model = Member
        fields = '__all__'



class ConversationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'


class GoldmemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goldmember
        fields = '__all__'