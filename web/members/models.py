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


# class Gender (models.Model):
#     gender =models.CharField( max_length=50)

#     def __str__(self) -> str:
#         return f'{self.gender}'

#     class Meta:
#         verbose_name = 'เพศสภาพ'


# class Testes (models.Model):
#     testes = models.CharField( max_length=50)

#     def __str__(self) -> str:
#         return f'{self.testes}'

#     class Meta:
#         verbose_name = 'รสนิยมทางเพศ'

# class Personality(models.Model):
#     personality = models.CharField(max_length=100) #ค่าการการทำนายจากการหาและคำนวนคะแนน (ขั่วบวกและขั่วลบ)

#     def __str__(self):
#         return self.personality

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    birthday = models.DateField(blank=True,null=True)
    age =  models.IntegerField(blank=True,null=True)
    GENDER = [('F', 'Female'),('M', 'Male')]
    gender = models.CharField( blank=True,null=True,choices=GENDER, max_length=1, default='F')
    testes = models.CharField( blank=True,null=True,choices=GENDER, max_length=1, default='M') # sex of Testes
    rasi = models.ForeignKey(RaSi, blank=True,null=True, verbose_name='ราศีประจำวันเกิด',on_delete=models.CASCADE)
    daysofweek = models.ForeignKey(DaysOfWeek, blank=True,null=True, verbose_name='วันประจำวันเกิด',on_delete=models.CASCADE)
    bloodtype = models.ForeignKey(BloodType, blank=True,null=True ,verbose_name="หมู่เลือด",on_delete=models.CASCADE)
    naksus = models.ForeignKey(NakSus, blank=True,null=True ,verbose_name="นักษัตร",on_delete=models.CASCADE)
    # personality = models.ManyToManyField(Personality,related_name='members',blank=True,null=True,) #ขั้วบวกลบ
    like = models.BooleanField(default=False)
    nope = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True) # When it was create
    updated = models.DateTimeField(auto_now=True)  # When it was update

    @property
    def calculate_age(self):
        if self.birthday:
            today = date.today()
            self.age = today.year - self.birthday.year
            return self.age
        print("It's Age Calculed: {{self.age}}")
        return self.age # when "self.birthday" is "NULL"

    def save(self, *args, **kwargs):
        if not self.id:
            today = date.today()
            self.age = today.year - self.birthday.year
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username},{self.user.first_name},{self.user.last_name} {self.age} {self.testes}'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Rating(models.Model):
    ratingUser = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='ratingUser')
    ratedUser = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='ratedUser')
    like = models.BooleanField()
    ratingPoint = models.IntegerField(null=True,blank=True)

    class Meta:
        unique_together = ('ratingUser', 'ratedUser')
    
    def __str__(self):
        return str(self.ratingUser) + ' ' + str(self.ratedUser) + ' ' + str(self.like)


class Match(models.Model):
    user1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user2')

    class Meta:
        unique_together = ('user1', 'user2')
        unique_together = ('user2', 'user1')
    def __str__(self):
        return str(self.user1) + ' ' + str(self.user2)
        
class Handler(models.Model):
    # block = models.BooleanField(default=False,blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rejected = models.BooleanField(default=False)
    reviewe_value = models.IntegerField(blank=True,null=True) # แสดงให้คนคุยมากกว่า 1 weeks or คนที่คุยกันมากกว่า 50 times
    created = models.DateTimeField(auto_now_add=True)  # When it was create
    updated = models.DateTimeField(auto_now=True)  # When i was update
    def __str__(self) -> str:
        return f' {self.reviewe_value} {self.rejected}'

    class Meta:
        verbose_name = "Handler"


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    text = models.CharField(max_length=280)
    sentDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.sender) + ' ' + str(self.recipient) + ' ' + self.text


# class Goldmember(models.Model):
#     goldmember = models.OneToOneField(
#         Profile,
#         null=True,blank=True,
#         on_delete=models.CASCADE,
#         # prsimary_key=True,
#         related_name='goldmember', related_query_name='goldmember'
    # )
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, related_query_name='conversation',
    #                                verbose_name='User_ID',
    #                                on_delete=models.CASCADE)
    # conversation = models.ForeignKey(Conversation,null=True,blank=True,
    #                                  verbose_name='Conversation_ID',
    #     on_delete=models.CASCADE)

    # def __str__(self) -> str:
    #     return f'{self.goldmember}'