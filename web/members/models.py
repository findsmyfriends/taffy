from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import date
from django.db.models.deletion import ProtectedError
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields import NullBooleanField
from django.db.models.fields.related import ForeignKey
from django.http import request
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Member(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    birthday = models.DateField(blank=True,null=True)
    class Meta:
        verbose_name = 'Member'


class BloodType(models.Model):

    bloodtype =models.CharField(max_length=10)
   
    

    def __str__(self) -> str:
        return self.bloodtype


class DaysOfWeek(models.Model):
    daysofweek = models.CharField(max_length=100)
    

    def __str__(self):
        return f'{self.daysofweek}'



class NakSus(models.Model):
    naksus = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.naksus}'



class RaSi(models.Model):
    rasi = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.rasi}'

def get_daysofweek():
    return DaysOfWeek.objects.get(id=1)
def get_naksus():
    return NakSus.objects.get(id=1)
def get_rasi():
    return RaSi.objects.get(id=1)
def get_bloodtype():
    return BloodType.objects.get(id=1)
 
class Profile(models.Model):
    GENDER = [('F', 'Female'),('M', 'Male')]
    # DAYSOfWEEK = [('SUN','Sunday'),('MON','Monday'),('TUE','Tuesday'),('WED','Wednesday'),('THU','Thursday'),('FRI','Friday'),('SAT','Saturday')]
    user = models.OneToOneField(Member,verbose_name='members', on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    birthday = models.DateField(blank=True,null=True)
    age =  models.IntegerField(blank=True,null=True)
    gender = models.CharField(choices=GENDER, max_length=1, default='F')
    testes = models.CharField(choices=GENDER, max_length=1, default='M') # sex of Testes
    daysofweek = models.ForeignKey(DaysOfWeek,  default=get_daysofweek,verbose_name='วันประจำวันเกิด',on_delete=models.CASCADE)
    naksus = models.ForeignKey(NakSus,default=get_naksus,verbose_name="นักษัตร",on_delete=models.CASCADE)
    rasi = models.ForeignKey(RaSi,  default=get_rasi,verbose_name='ราศี',on_delete=models.CASCADE)
    bloodtype = models.ForeignKey(BloodType, default=get_bloodtype,verbose_name="หมู่เลือด",on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True) # When it was create
    updated = models.DateTimeField(auto_now=True)  # When it was update
    # personality = models.ManyToManyField(Personality,related_name='members',blank=True,null=True,) #ขั้วบวกลบ

    def __str__(self):
        return f'{self.user.username} {self.user.email} {self.age} '

    def save(self, *args, **kwargs):
        
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
            
        if self.daysofweek:
            try:
                daysoftheweek = self.birthday.strftime( '%A' )
                if daysoftheweek == 'Sunday':
                    self.daysofweek_id = 1 
                    
                elif daysoftheweek == 'Monday':
                    self.daysofweek_id = 2
                    
                elif daysoftheweek == 'Tuesday':
                    self.daysofweek_id = 3
                    
                elif daysoftheweek == 'Wednesday':
                    self.daysofweek_id = 4
                    
                elif daysoftheweek == 'Thursday':
                    self.daysofweek_id = 5
                    
                elif daysoftheweek == 'Friday':
                    self.daysofweek_id = 6
                    
                elif daysoftheweek == 'Saturday':
                    self.daysofweek_id = 7
                    
            except:
                daysoftheweek = None
        # print('_______day of date________',self.birthday.strftime( '%A' ))

        if self.naksus:
            try:
                year = self.birthday.year
                print(f'_______self.birthday.year_______{type(year)}__________{year}')
                # if year == 2020 and  year == 2008 and   year == 1996 and   year ==1984 and   year == 1972 and   year == 1960:
                if year == 2020 or  year == 2008 or year == 1996 or year == 1984 or year == 1972 or year ==  1960:
                    self.naksus_id = 1
                    
                elif year ==  2021 or year == 2009 or year == 1997 or year == 1985 or year == 1973 or year == 1961:
                    self.naksus_id = 2
                    
                elif year == 2022 or year == 2010 or year == 1998 or year == 1986 or year == 1974 or year == 1962:
                    self.naksus_id = 3
                    
                elif year == 2023 or year == 2011 or year == 1999 or year == 1987 or year == 1975 or year == 1963:
                    self.naksus_id = 4
                    
                elif year == 2024 or year == 2012 or year == 2000 or year == 1988 or year == 1976 or year == 1964:
                    self.naksus_id = 5
                    
                elif year ==2025 or year == 2013 or year == 2001 or year == 1989 or year == 1977 or year == 1965:
                    self.naksus_id = 6
                    
                elif year == 2026 or year == 2014 or year == 2002 or year == 1990 or year == 1978 or year == 1966:
                    self.naksus_id = 7
                    
                elif year ==  2027 or year == 2015 or year == 2003 or year == 1991 or year == 1979 or year == 1967:
                    self.naksus_id = 8
                    
                elif year == 2028 or year == 2016 or year == 2004 or year == 1992 or year == 1980 or year == 1968:
                    self.naksus_id = 9
                    
                elif year == 2029 or year == 2017 or year == 2005 or year == 1993 or year == 1981 or year == 1969:
                    self.naksus_id = 10
                    
                elif year == 2030 or year == 2018 or year == 2006 or year == 1994 or year == 1982 or year == 1970:
                    self.naksus_id = 11
                    
                elif year == 2031 or year == 2019 or year == 2007 or year == 1995 or year == 1983 or year == 1971:
                    self.naksus_id = 12
                    
            except:
                year = None
        # print(f'_______self.birthday.year_______{self.naksus}__________{year}_______{self.naksus_id}')
        if self.rasi:
            # pass
            try:
                rasi = self.birthday
                print(rasi.day)
                if ((int(rasi.month)==12 and int(rasi.day) >= 16) or (int(rasi.month)==1 and int(rasi.day)<= 14)):
                    self.rasi_id = 12
                    
                elif ((int(rasi.month)==1 and int(rasi.day) >= 15)or(int(rasi.month)==2 and int(rasi.day)<= 12)):
                    self.rasi_id = 1
                    
                elif ((int(rasi.month)==2 and int(rasi.day) >= 13)or(int(rasi.month)==3 and int(rasi.day)<= 14)):
                    self.rasi_id = 2
                    
                elif ((int(rasi.month)==3 and int(rasi.day) >= 15)or(int(rasi.month)==4 and int(rasi.day)<= 12)):
                    self.rasi_id = 3
                    
                elif ((int(rasi.month)==4 and int(rasi.day) >= 13)or(int(rasi.month)==5 and int(rasi.day)<= 14)):
                    self.rasi_id = 4
                    
                elif ((int(rasi.month)==5 and int(rasi.day) >= 15)or(int(rasi.month)==6 and int(rasi.day)<= 14)):
                    self.rasi_id = 5
                    
                elif ((int(rasi.month)==6 and int(rasi.day) >= 15)or(int(rasi.month)==7 and int(rasi.day)<= 14)):
                    self.rasi_id = 6
                    
                elif ((int(rasi.month)==7 and int(rasi.day) >= 15)or(int(rasi.month)==8 and int(rasi.day)<= 15)): 
                    self.rasi_id = 7
                    
                elif ((int(rasi.month)==8 and int(rasi.day) >= 16)or(int(rasi.month)==9 and int(rasi.day)<= 16)): 
                    self.rasi_id = 8
                    
                elif ((int(rasi.month)==9 and int(rasi.day) >= 17)or(int(rasi.month)==10 and int(rasi.day)<= 15)):
                    self.rasi_id = 9
                    
                elif ((int(rasi.month)==10 and int(rasi.day) >= 17)or(int(rasi.month)==11 and int(rasi.day)<= 15)): 
                    self.rasi_id = 10
                    
                elif ((int(rasi.month)==11 and int(rasi.day) >= 16)or(int(rasi.month)==12 and int(rasi.day)<= 15)):
                    self.rasi_id = 11
                          
            except:
                rasi = None

        print(f'_______self.rasi_______{self.rasi}__________{year}_______')
        super(Profile, self).save(*args, **kwargs)


class Rating(models.Model):
    reqUser = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reqUser')
    ratedUser = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='ratedUser')
    ratingPoint = models.IntegerField(null=True,blank=True)
    # like = models.BooleanField()

    class Meta:
        unique_together = ('reqUser', 'ratedUser')
    
    def __str__(self):
        return f' {self. reqUser} {self.ratedUser} (Point: {self.ratingPoint})'
       


class Match(models.Model):
    # user1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user1')
    user1 = models.ForeignKey(Member, on_delete=models.CASCADE,related_name='user1')
    user2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user2')

    class Meta:
        unique_together = ('user1', 'user2')
        unique_together = ('user2', 'user1')
    def __str__(self):
        return str(self.user1) + ' ' + str(self.user2)
        
class Handler(models.Model):
    # block = models.BooleanField(default=False,blank=True,null=True)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    rejected = models.BooleanField(default=False)
    reviewe_value = models.IntegerField(blank=True,null=True) # แสดงให้คนคุยมากกว่า 1 weeks or คนที่คุยกันมากกว่า 50 times
    created = models.DateTimeField(auto_now_add=True)  # When it was create
    updated = models.DateTimeField(auto_now=True)  # When i was update
    def __str__(self) -> str:
        return f' {self.reviewe_value} {self.rejected}'

    class Meta:
        verbose_name = "Handler"


class Message(models.Model):
    sender = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='recipient')
    text = models.CharField(max_length=280)
    sentDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.sender) + ' ' + str(self.recipient) + ' ' + self.text


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

# class ScoreOfBloodType(models.Model):
#     memberA = models.ForeignKey(BloodType,on_delete=models.CASCADE,related_name='column_item')
#     memberB = models.ForeignKey(BloodType,on_delete=models.CASCADE,related_name='row_item')
#     score = models.IntegerField()
    
#     def __str__(self):
#         return str(self.memberA) + ' ' + str(self.memberB) + ' ' + str(self.score)
        

# class ScoreOfDaysOfWeek(models.Model):
#     memberA = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='daysofweek_pk_req')
#     memberB = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='daysofweek_pk_all')
#     score = models.IntegerField()
    
#     def __str__(self):
#         return str(self.memberA) + ' ' + str(self.memberB) + ' ' + str(self.score)

# class ScoreOfNakSus(models.Model):
#     memberA = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='naksus_pk_req')
#     memberB = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='naksus_pk_all')
#     score = models.IntegerField()

#     def __str__(self):
#         return str(self.memberA) + ' ' + str(self.memberB) + ' ' + str(self.score)
# class ScoreOfRaSi(models.Model):
#     memberA = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='rasi_pk_req')
#     memberB = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='rasi_pk_all')
#     score = models.IntegerField()
#     def __str__(self):
#         return str(self.memberA) + ' ' + str(self.memberB) + ' ' + str(self.score)