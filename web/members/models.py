from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import date
from django.db.models.deletion import ProtectedError
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields import NullBooleanField
from django.db.models.fields.related import ForeignKey


class BloodType(models.Model):

    bloodtype =models.CharField(max_length=10)
   
    

    def __str__(self) -> str:
        return self.bloodtype

    # class Meta:
    #     verbose_name = 'หมู่เลือด'


class DaysOfWeek(models.Model):
    daysofweek = models.CharField(max_length=100)
    

    def __str__(self):
        return f'{self.daysofweek}'

    # class Meta:
    #     verbose_name = 'วันประจำวันเกิด'


class NakSus(models.Model):
    naksus = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.naksus}'

    # class Meta:
    #     verbose_name = 'นักษัตร'


class RaSi(models.Model):
    rasi = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.rasi}'

    # class Meta:
    #     verbose_name = 'ราศี'


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
    GENDER = [('F', 'Female'),('M', 'Male')]
    DAYSOfWEEK = [('SUN','Sunday'),('MON','Monday'),('TUE','Tuesday'),('WED','Wednesday'),('THU','Thursday'),('FRI','Friday'),('SAT','Saturday')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    birthday = models.DateField(blank=True,null=True)
    age =  models.IntegerField(blank=True,null=True)
    gender = models.CharField( blank=True,null=True,choices=GENDER, max_length=1, default='F')
    testes = models.CharField( blank=True,null=True,choices=GENDER, max_length=1, default='M') # sex of Testes
    rasi = models.ForeignKey(RaSi, blank=True,null=True, verbose_name='ราศีประจำวันเกิด',on_delete=models.CASCADE)
    bloodtype = models.ForeignKey(BloodType, blank=True,null=True ,verbose_name="หมู่เลือด",on_delete=models.CASCADE)
    naksus = models.ForeignKey(NakSus, blank=True,null=True ,verbose_name="นักษัตร",on_delete=models.CASCADE)
    daysofweek = models.ForeignKey(DaysOfWeek, blank=True,null=True, verbose_name='วันประจำวันเกิด',on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    nope = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True) # When it was create
    updated = models.DateTimeField(auto_now=True)  # When it was update
    # personality = models.ManyToManyField(Personality,related_name='members',blank=True,null=True,) #ขั้วบวกลบ

    def __str__(self):
        return f'{self.user.username} {self.age} {self.testes} {self.daysofweek} {self.naksus} {self.rasi} {self.bloodtype}'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        # DAYSOfWEEK = [('SUN','Sunday'),('MON','Monday'),('TUE','Tuesday'),('WED','Wednesday'),('THU','Thursday'),('FRI','Friday'),('SAT','Saturday')]
        if self.birthday:
            today = date.today()
            self.age = today.year - self.birthday.year
            print("models save auto", self.age )
            super(Profile, self).save(*args, **kwargs)
        # if self.daysofweek:
        #     daysoftheweek = self.birthday.strftime( '%A' )
            
        #     if daysoftheweek == 'Sunday':
                
        #         self.daysofweek.pk = 1 
        #         super(Profile, self).save(*args, **kwargs)
        #     if daysoftheweek == 'Monday':
        #         print("MON")
        #         self.daysofweek.pk = 2
        #         super(Profile, self).save(*args, **kwargs)
        # # self.daysofweek.pk = 1
        
        # print('_______day of date________',self.birthday.strftime( '%A' ))


class ScoreOfBloodType(models.Model):
    memberA = models.ForeignKey(BloodType,on_delete=models.CASCADE,related_name='column_item')
    memberB = models.ForeignKey(BloodType,on_delete=models.CASCADE,related_name='row_item')
    score = models.IntegerField()
    
    def __str__(self):
        return str(self.memberA) + ' ' + str(self.memberB) + ' ' + str(self.score)
        

class ScoreOfDaysOfWeek(models.Model):
    memberA = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='daysofweek_pk_req')
    memberB = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='daysofweek_pk_all')
    score = models.IntegerField()
    
    def __str__(self):
        return str(self.memberA) + ' ' + str(self.memberB) + ' ' + str(self.score)

class ScoreOfNakSus(models.Model):
    memberA = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='naksus_pk_req')
    memberB = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='naksus_pk_all')
    score = models.IntegerField()

    def __str__(self):
        return str(self.memberA) + ' ' + str(self.memberB) + ' ' + str(self.score)
class ScoreOfRaSi(models.Model):
    memberA = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='rasi_pk_req')
    memberB = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='rasi_pk_all')
    score = models.IntegerField()
    def __str__(self):
        return str(self.memberA) + ' ' + str(self.memberB) + ' ' + str(self.score)

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

