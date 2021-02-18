from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import date

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

class Personality(models.Model):
    personality = models.CharField(max_length=100) #ค่าการการทำนายจากการหาและคำนวนคะแนน (ขั่วบวกและขั่วลบ)

    def __str__(self):
        return self.value

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    birthday = models.DateField(blank=True,null=True)
    age =  models.IntegerField(blank=True,null=True)
    rasi = models.ForeignKey(RaSi,  blank=True,null=True,verbose_name='ราศีประจำวันเกิด',on_delete=models.CASCADE)
    bloodtype = models.ForeignKey(BloodType,  blank=True,null=True,verbose_name="หมู่เลือด",on_delete=models.CASCADE)
    naksus = models.ForeignKey(NakSus,  blank=True,null=True,verbose_name="นักษัตร",on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, blank=True,null=True,verbose_name="เพศ",on_delete=models.CASCADE)
    testes = models.ForeignKey(Testes, blank=True,null=True,verbose_name="รสนิยมทางเพศ",on_delete=models.CASCADE)  # sex of Testes
    personality = models.ManyToManyField(Personality,related_name='members',blank=True,null=True,) #ขั้วบวกลบ
    like = models.BooleanField(default=False,blank=True,null=True)
    nope = models.BooleanField(default=False,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True) # When it was create
    updated = models.DateTimeField(auto_now=True)  # When it was update

    @property
    def calculate_age(self):
        if self.birthday:
            today = date.today()
            self.age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
            return self.age
        return 0  # when "self.birthday" is "NULL"

    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

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
    # profile = models.ForeignKey(Profile, related_query_name='conversation',
    #                                verbose_name='Conversations_ID',
    #                                on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_query_name='conversation',
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
        Profile,
        null=True,blank=True,
        on_delete=models.CASCADE,
        # prsimary_key=True,
        related_name='goldmember', related_query_name='goldmember'
    )
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, related_query_name='conversation',
    #                                verbose_name='User_ID',
    #                                on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation,null=True,blank=True,
                                     verbose_name='Conversation_ID',
        on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.goldmember}'