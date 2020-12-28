from django.contrib.admin.sites import DefaultAdminSite
from django.db import models
from django.db.models.deletion import CASCADE


class BloodType(models.Model):
   
    bloodtype =models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f'{self.bloodtype}'

class DayOfBirth(models.Model):
    dayofbirth = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.dayofbirth}'


class NakSus(models.Model):
    naksus = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.naksus}'

class RaSi(models.Model):
    rasi = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.rasi}'


class Birthday(models.Model):
    defaulAge = int(18)  
    age = models.IntegerField(default=DayOfBirth)
    birthday = models.DateField(auto_now=True)
    dayofbirth = models.ForeignKey(DayOfBirth,on_delete=models.CASCADE)
    rasi = models.ForeignKey(RaSi,on_delete=models.CASCADE)
    bloodtype = models.ForeignKey(BloodType,on_delete=models.CASCADE)
    naksus = models.ForeignKey(NakSus,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.birthday} {self.age}'

class Sexual(models.Model):
    sexual = models.CharField(max_length=100)
    
    
    def __str__(self) -> str:
        return f'{self.sexual}'

class SexTest(models.Model):
    sextest = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.sextest}'


class Member(models.Model):
    email = models.EmailField( max_length=564)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    birthday = models.ForeignKey(Birthday, on_delete=models.CASCADE)
    sexaul = models.ForeignKey(Sexual,on_delete=models.CASCADE)
    sextest = models.ForeignKey(SexTest,on_delete=models.CASCADE)
    profile = models.TextField(blank=True ,default="")
    discription = models.CharField(max_length=1000,default="")
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}  '

class PictureURL(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    picurl = models.TextField(blank=True ,default="")
    discription = models.CharField(max_length=1000,default="")
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update

    def __str__(self):
        return f'{self.discription}'

class LikeMembers (models.Model):
    # pass
    member = models.ForeignKey(Member,on_delete=models.CASCADE)

class LikeOfAll(models.Model):
    likeUall = models.BooleanField(default=True)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    addscroce = models.IntegerField(10)

    def __str__(self):
        return f'{self.likeUall}'

class NopeOfALl(models.Model):
    nopeUall = models.BooleanField(default=True)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    deductscroce = models.IntegerField(-10)

    def __str__(self):
        return f'{self.nopeUall} {self.deductscroce}'
    

class Goldmember(models.Model):
    goldmember = models.ForeignKey(Member, on_delete=models.CASCADE)
    likeUall = models.ForeignKey(LikeOfAll,on_delete=models.CASCADE)
    # goldmember = models.ManyToManyField(LikeOfAll)
    # displayLikeyou = 



class Matched(models.Model):
    birthday = models.ForeignKey(Birthday, on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.birthday} {self.member}'

class FilterType(models.Model):
    filttertype =models.CharField(max_length=20)

    def __str__(self):
        return f'{self.filttertype}'

class FilteredBy (models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    age = models.ForeignKey(Birthday,on_delete=models.CASCADE)
    filtertype =models.ForeignKey(FilterType,on_delete=models.CASCADE)


class Conversations(models.Model):
    # 
    newmember = models.ForeignKey(Member,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update

class Participant (models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversations,on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update

class Message(models.Model):
    participant_id = models.ForeignKey(Participant,on_delete=models.CASCADE)
    message_text = models.TextField(blank=True ,default="")
    time_at = models.DateTimeField(auto_now_add=True) # When it was create

    def __str__(self):
        return self.message_text