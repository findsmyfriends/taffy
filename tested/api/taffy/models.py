from django.db import models
from datetime import date, timedelta
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeCheckMixin, DateTimeField

from versatileimagefield.fields import VersatileImageField, PPOIField

class BloodType(models.Model):

    bloodtype =models.CharField(max_length=10)

    def __str__(self) -> str:
        return f'{self.bloodtype}'

    class Meta:
        verbose_name = 'หมู่เลือด'


class DaysOfWeek(models.Model):
    daysofweek = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.daysofweek}'

    class Meta:
        verbose_name = 'วันประจำวันเกิด'


class NakSus(models.Model):
    naksus = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.naksus}'

    class Meta:
        verbose_name = 'นักษัตร'


class RaSi(models.Model):
    rasi = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.rasi}'

    class Meta:
        verbose_name = 'ราศี'


class Gender (models.Model):
    gender =models.CharField( max_length=50)

    def __str__(self) -> str:
        return f'{self.gender}'

    class Meta:
        verbose_name = 'เพศ'


class Testes (models.Model):
    testes = models.CharField( max_length=50)

    def __str__(self) -> str:
        return f'{self.testes}'

    class Meta:
        verbose_name = 'รสนิยมทางเพศ'

class AgeManage(models.Manager):
    def calAge(self):
        age     = models.IntegerField()
        today = date.today()
        agecal =  today.year - age.year - ((today.month, today.day) < (age.month, age.day))
        age.add(agecal)
    
class Image(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return self.name




class Member(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='members', related_query_name='members')
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    birthday = models.DateField(auto_now=False)
    age =  models.IntegerField(blank=True,null=True)
    dayofbirth = models.ForeignKey(DaysOfWeek, blank=True,null=True,verbose_name="วันประจำวันเกิด",on_delete=models.CASCADE)
    rasi = models.ForeignKey(RaSi,  blank=True,null=True,verbose_name='ราศีประจำวันเกิด',on_delete=models.CASCADE)
    bloodtype = models.ForeignKey(BloodType,  blank=True,null=True,verbose_name="หมู่เลือด",on_delete=models.CASCADE)
    naksus = models.ForeignKey(NakSus,  blank=True,null=True,verbose_name="นักษัตร",on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, blank=True,null=True,verbose_name="เพศ",on_delete=models.CASCADE)
    testes = models.ForeignKey(Testes, blank=True,null=True,verbose_name="รสนิยมทางเพศ",on_delete=models.CASCADE)  # sex of Testes
    image = models.ManyToManyField('taffy.Image', related_name='members')
    profileurl = models.TextField(blank=True,null=True,default="")
    discription = models.CharField(max_length=1000,default="",blank=True,null=True)
    characterneed = models.IntegerField(blank=True,null=True)# ลักษณนิสัย คะแนน ที่เป็น ขั้วบวก = 1,ขั้วลบ =0 ที่ต้องการ
    values = models.IntegerField(blank=True,null=True) # like = 1 nope =0
    created = models.DateTimeField(auto_now_add=True) # When it was create
    updated = models.DateTimeField(auto_now=True)  # When it was update
    

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} '

    class Meta:
        verbose_name = 'Member Profiles'
        ordering = ['-created']
        
class Conversation(models.Model):
    member = models.ForeignKey(Member,
                                   verbose_name='Conversations',
                                   on_delete=models.CASCADE)
    message = models.TextField(blank=True ,null=True)
    block = models.BooleanField(default=False,blank=True,null=True)
    rejected = models.BooleanField(default=False, blank=True, null=True)
    reviewe_value = models.IntegerField(blank=True,null=True) # แสดงให้คนคุยมากกว่า 1 weeks or คนที่คุยกันมากกว่า 50 times
    joined_at = models.DateTimeField(auto_now_add=False)  # When it was create
    updated_at = models.DateTimeField(auto_now=False)  # When i was update

    def __str__(self) -> str:
        return f'{self.member}  {self.block} {self.rejected}'

    class Meta:
        verbose_name = "สนทนา"

class LikeNopeManager(models.Manager):
    def like_toggle(self, member, pro_obj):
        if member in pro_obj.liked.all():
            is_liked = False
            pro_obj.liked.remove(member)
        else:
            is_liked = True
            pro_obj.liked.add(member)
        return is_liked

    def nope_toggle(self, member, pro_obj):
        if member in pro_obj.noped.all():
            is_nope = False
            pro_obj.noped.remove(member)
        else:
            is_nope = True
            pro_obj.noped.add(member)
        return is_nope

class Goldmember(models.Model):
    member = models.ForeignKey(Member,
                                   verbose_name='Goldmember',
                                   on_delete=models.CASCADE)
    liked = models.ManyToManyField(
        Member, blank=True, related_name='liked')
    noped = models.ManyToManyField(
        Member, blank=True, related_name='noped')

    object = LikeNopeManager()
    conversation = models.ForeignKey(Conversation,
                                     verbose_name=' block & rejected :',
                                     on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.goldmember} {self.conversation}'
