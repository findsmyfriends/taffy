from django.db import models

# Create your models here.
from django.db.models.deletion import CASCADE


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


# class PictureURL(models.Model):
#     picpost = models.TextField(blank=True, default="")
#     discription = models.CharField(max_length=1000, default="")
#     created_at = models.DateTimeField(auto_now_add=True)  # When it was create
#     updated_at = models.DateTimeField(auto_now=True)  # When i was update

#     def __str__(self):
#         return f'{self.discription}'


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

class Member(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField( max_length=564)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    birthday = models.DateField(auto_now=False)
    age = models.IntegerField()
    dayofbirth = models.ForeignKey(DaysOfWeek, verbose_name="วันประจำวันเกิด",on_delete=models.CASCADE)
    rasi = models.ForeignKey(RaSi, verbose_name='ราศีประจำวันเกิด',on_delete=models.CASCADE)
    bloodtype = models.ForeignKey(BloodType, verbose_name="หมู่เลือด",on_delete=models.CASCADE)
    naksus = models.ForeignKey(NakSus, verbose_name="นักษัตร",on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender,verbose_name="เพศ",on_delete=models.CASCADE)
    testes = models.ForeignKey(Testes,verbose_name="รสนิยมทางเพศ",on_delete=models.CASCADE)  # sex of Testes
    profileurl = models.TextField(blank=True,null=True,default="")
    discription = models.CharField(max_length=1000,default="",blank=True,null=True)
    characterneed = models.IntegerField()# ลักษณนิสัย คะแนน ที่เป็น ขั้วบวก = 1,ขั้วลบ =0 ที่ต้องการ
    values = models.IntegerField(blank=True,null=True) # like = 1 nope =0
    created_at = models.DateTimeField(auto_now_add=False) # When it was create
    updated_at = models.DateTimeField(auto_now=False)  # When it was update

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} '



class Conversation(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
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


class Goldmember(models.Model):
    goldmember = models.ForeignKey(Member,
                                   verbose_name='Goldmember',
                                   on_delete=models.CASCADE)
    # values = models.ForeignKey(ValuesOfall, verbose_name=id,on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation,
                                     verbose_name=' block & rejected :',
                                     on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.goldmember} {self.conversation}'
