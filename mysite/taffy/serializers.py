
from rest_framework import serializers
from .models import Member
class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class  Meta:
        model = Member
        fields = ['first_name','last_name']
        # fields = ['first_name','last_name','birth','discription','sexual','sextest','link_pic','age']
    
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']