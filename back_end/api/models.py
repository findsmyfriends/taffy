from django.contrib.admin.sites import DefaultAdminSite
from django.db import models
from django.db.models.deletion import CASCADE
# import birthday
# Create your models here.

       
class Birthday(models.Model):
    defaulAge = int(18)
   
    age = models.models.IntegerField()
    birthday = models.DateField(auto_now=True)
    dayofbirth = models.CharField(max_length=20)
    rasi = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f'{self.birthday} {self.age}'


class Member(models.Model):
    email = models.EmailField( max_length=254)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    birthday = models.ForeignKey(Birthday, on_delete=models.CASCADE)
    sexual = models.BooleanField(default=True)
    sextest = models.BooleanField(default=True)
    link_pic = models.TextField(blank=True ,default="")
    discription = models.CharField(max_length=1000,default="")
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.sexual} '

    

class Goldmember(models.Model):
    pass

class Matched(models.Model):
    dayofbirth = models.ForeignKey(Birthday,on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.dayofbirth} {self.member}'


# class Match(models.Model):
    
#     daybirth =models.CharField(max_length=100)
#     range_age = models.IntegerField()
#     nuksus = models.CharField(max_length=100)


# class Filtter(models.Model):
#     anode = models.BooleanField(default=True)
#     cathhode = models.BooleanField(default=False)
#     range_age = models.IntegerField()
#     age = models.IntegerField()
#     like_val = models.BooleanField(default=True)
#     nope_val = models.BooleanField(default=False)

  