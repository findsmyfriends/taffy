from django.db import models

# Create your models here.
from django.db.models.deletion import CASCADE

class BloodType(models.Model):

    bloodtype =models.CharField(max_length=10)

    def __str__(self) -> str:
        return f'{self.bloodtype}'

class DaysofWeek(models.Model):
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


class PictureURL(models.Model):
    picpost = models.TextField(blank=True, default="")
    discription = models.CharField(max_length=1000, default="")
    created_at = models.DateTimeField(auto_now_add=True)  # When it was create
    updated_at = models.DateTimeField(auto_now=True)  # When i was update

    def __str__(self):
        return f'{self.discription}'


class Member(models.Model):
    email = models.EmailField( max_length=564)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    birthday = models.DateField(auto_now=True)
    age = models.IntegerField(default=DaysofWeek)
    dayofbirth = models.ForeignKey(DaysofWeek,  verbose_name=id,on_delete=models.CASCADE)
    rasi = models.ForeignKey(RaSi, verbose_name=id,on_delete=models.CASCADE)
    bloodtype = models.ForeignKey(BloodType, verbose_name=id,on_delete=models.CASCADE)
    naksus = models.ForeignKey(NakSus, verbose_name=id,on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    testes = models.CharField(max_length=100) # sex of Testes
    # profileurl = models.TextField(blank=True ,default="")
    profileurl = models.ForeignKey(PictureURL, verbose_name=id,on_delete=models.CASCADE)
    discription = models.CharField(max_length=1000,default="")
    characterneed = models.IntegerField()# ลักษณนิสัย คะแนน ที่เป็น ขั้วบวก = 1,ขั้วลบ =0 ที่ต้องการ
    values = models.IntegerField() # like = 1 nope =0
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When it was update

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} '


class Conversation(models.Model):
    member = models.ForeignKey(Member,verbose_name=id,on_delete=models.CASCADE)
    message = models.TextField(blank=True ,default="")
    block = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    reviewe_value = models.IntegerField() # แสดงให้คนคุยมากกว่า 1 weeks or คนที่คุยกันมากกว่า 50 times
    joined_at = models.DateTimeField(auto_now_add=True)  # When it was create
    updated_at = models.DateTimeField(auto_now=True)  # When i was update

    def __str__(self) -> str:
        return f'{self.reviewe_value} {self.messge}'


class ValuesOfall(models.Model): #แยกเพราะคิดว่าจะได้ใช้ id ValuesOfall and id Member ==> Primary Key
    member = models.ForeignKey(Member, verbose_name=id,on_delete=models.CASCADE)
    like = models.IntegerField()
    nope = models.IntegerField()

    def __str__(self):
        return f'{self.like}'


class Goldmember(models.Model):
    goldmember = models.ForeignKey(Member, verbose_name=id,on_delete=models.CASCADE)
    values = models.ForeignKey(ValuesOfall, verbose_name=id,on_delete=models.CASCADE)
    conversation =models.ForeignKey(Conversation, verbose_name=id,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'
