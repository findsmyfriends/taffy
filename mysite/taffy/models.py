from django.db import models

# Create your models here.
class Member(models.Model):
    # id_ = models.AutoField(primary_key=True)
    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    birth = models.DateField(auto_now=True)
    discription = models.CharField(max_length=1000,default="")
    sexual = models.CharField(max_length=100)
    sextest = models.CharField(max_length=100)
    link_pic = models.TextField(blank=True ,default="")
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update
    
    # class Meta:
    #     ordering = ['created_at']


class Filtter(models.Model):
    # _id = models.AutoField(primary_key=True)
    # user_id = models.AutoField(unique=True)
    anode = models.BooleanField(default=True)
    cathhode = models.BooleanField(default=False)
    range_age = models.IntegerField()
    age = models.IntegerField()
    like_val = models.BooleanField(default=True)
    nope_val = models.BooleanField(default=False)

class Match(models.Model):
    
    daybirth =models.CharField(max_length=100)
    range_age = models.IntegerField()
    nuksus = models.CharField(max_length=100)




  