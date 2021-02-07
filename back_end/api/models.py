from django.db import models
from datetime import date
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Value
from versatileimagefield.fields import VersatileImageField, PPOIField
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class BloodType(models.Model):

    bloodtype =models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.bloodtype

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
        verbose_name = 'เพศสภาพ'


class Testes (models.Model):
    testes = models.CharField( max_length=50)

    def __str__(self) -> str:
        return f'{self.testes}'

    class Meta:
        verbose_name = 'รสนิยมทางเพศ'


class Image(models.Model):
    des = models.CharField(max_length=255,verbose_name="Description")
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return self.des

    class Meta:
        verbose_name = 'ImageProfile'


class Personality(models.Model):
    value = models.CharField(max_length=100) #ค่าการการทำนายจากการหาและคำนวนคะแนน (ขั่วบวกและขั่วลบ) 
    
    def __str__(self):
        return self.value


class NopedManager(models.Manager):
    def nope_toggle(self, user, pro_obj):
        if user in pro_obj.noped.all():
            is_nope = False
            pro_obj.noped.remove(user)
        else:
            is_nope = True
            pro_obj.noped.add(user)
        return is_nope

class LikedManager(models.Manager):
    def like_toggle(self, user, pro_obj):
        if user in pro_obj.liked.all():
            is_liked = False
            pro_obj.liked.remove(user)
        else:
            is_liked = True
            pro_obj.liked.add(user)
        return is_liked

class MemberProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='members', related_query_name='members'
    )
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='members', related_query_name='members')
    first_name = models.CharField(max_length=500,blank=True,null=True)
    last_name = models.CharField(max_length=500,blank=True,null=True)
    birthday = models.DateField()
    age =  models.IntegerField(blank=True,null=True)
    dayofbirth = models.ForeignKey(DaysOfWeek, blank=True,null=True,verbose_name="วันประจำวันเกิด",on_delete=models.CASCADE)
    rasi = models.ForeignKey(RaSi,  blank=True,null=True,verbose_name='ราศีประจำวันเกิด',on_delete=models.CASCADE)
    bloodtype = models.ForeignKey(BloodType,  blank=True,null=True,verbose_name="หมู่เลือด",on_delete=models.CASCADE)
    naksus = models.ForeignKey(NakSus,  blank=True,null=True,verbose_name="นักษัตร",on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, blank=True,null=True,verbose_name="เพศ",on_delete=models.CASCADE)
    testes = models.ForeignKey(Testes, blank=True,null=True,verbose_name="รสนิยมทางเพศ",on_delete=models.CASCADE)  # sex of Testes
    imageprofile = models.ManyToManyField('api.Image', related_name='members')
    imageprofile2 =  VersatileImageField(
        'ImageProflie',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()
    personality = models.ManyToManyField('api.Personality',related_name='members')
    liked = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='liked')
    noped = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='noped')
    created = models.DateTimeField(auto_now_add=True) # When it was create
    updated = models.DateTimeField(auto_now=True)  # When it was update
    objects = LikedManager()
    objects = NopedManager()

    
    def save(self, *args, **kwargs):
        if not self.id:
            today = date.today()
            self.first_name = self.user.first_name 
            self.last_name = self.user.last_name
            self.age = today.year - self.birthday.year
        super(MemberProfile, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.id}:  {self.user} {self.first_name} {self.last_name} '

    class Meta: 
        verbose_name = 'ProfileMember'
        ordering = ['-created']

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MemberProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.memberprofile.save()



class Handler(models.Model):
    # block = models.BooleanField(default=False,blank=True,null=True)
    rejected = models.BooleanField(default=False, blank=True, null=True)
    reviewe_value = models.IntegerField(blank=True,null=True) # แสดงให้คนคุยมากกว่า 1 weeks or คนที่คุยกันมากกว่า 50 times
    created = models.DateTimeField(auto_now_add=True)  # When it was create
    updated = models.DateTimeField(auto_now=True)  # When i was update
    def __str__(self) -> str:
        return f' {self.reviewe_value} {self.rejected}'

    class Meta:
        verbose_name = "Handler"


class Conversation(models.Model):
    memberprofile = models.ForeignKey(MemberProfile, related_query_name='conversation',
                                   verbose_name='Conversations_ID',
                                   on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_query_name='conversation',
                                   verbose_name='User_ID',
                                   on_delete=models.CASCADE)
    message  = models.TextField(blank=True ,null=True)
    rejected =models.ForeignKey(Handler, blank=True ,null=True,related_query_name='conversation',
                                   verbose_name='Rejected',
                                   on_delete=models.CASCADE)
                           
    created = models.DateTimeField(auto_now_add=True)  # When it was create
    updated = models.DateTimeField(auto_now=True)  # When i was update


  

    def __str__(self) -> str:
        return f'{self.member}  {self.block} {self.rejected}'

    class Meta:
        verbose_name = "Conversation"   


class Goldmember(models.Model):
    goldmember = models.OneToOneField(
        MemberProfile,
        null=True,blank=True,
        on_delete=models.CASCADE,
        # primary_key=True,
        related_name='goldmember', related_query_name='goldmember'
    )   

    conversation = models.ForeignKey(Conversation,null=True,blank=True,
                                     verbose_name='Conversation_ID',
        on_delete=models.CASCADE)
                        
    def __str__(self) -> str:
        return f'{self.goldmember}'


