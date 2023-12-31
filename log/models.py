from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your models here.

class varieties(models.Model):
    type_no=models.IntegerField()
    type_name=models.CharField(max_length=10)
    def __str__(self):
        return self.type_name
    
mode_choice=(('online','online'),('offline','offline'))
class Event(models.Model):
    event_name=models.CharField( max_length=20)
    instruction=models.CharField(max_length=1000)
    category=models.ForeignKey(varieties,on_delete=models.CASCADE)
    date=models.DateField()
    mode=models.CharField( max_length=10,  choices=mode_choice)
    registration_fee=models.IntegerField()
    prize_amount=models.IntegerField()
    contact_number=models.BigIntegerField()
    duration=models.TimeField()
    venue=models.CharField(max_length=50)
    def __str__(self):
        return self.event_name
  
gender_choice=(("male","male"),("female","female"))  
year_option=(("First year","First year"),("Second year","Second year"),("Third year","Third year"),("Final year","Final year"))

# class register(models.Model):
#     
#      email_address=models.EmailField()
#    events_name=models.ForeignKey(Event,on_delete=models.CASCADE)
#     
    
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    yugam_id=models.BigAutoField(primary_key = True)
    email_address=models.EmailField(unique=True)
    gender=models.CharField(max_length=10,choices=gender_choice)
    mobile=models.BigIntegerField()
    college=models.CharField(max_length=30)
    year_of_study=models.CharField(max_length=15,choices=year_option)
    
    
class Workshop(models.Model):
    workshop_name=models.CharField( max_length=20)
    description=models.CharField(max_length=1000)
    category=models.ForeignKey(varieties,on_delete=models.CASCADE)
    date=models.DateField()
    registration_fee=models.IntegerField() 
    contact_number=models.BigIntegerField()
    duration=models.TimeField()
    venue=models.CharField(max_length=50)
    def __str__(self):
        return self.workshop_name
    
class registeration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    event_or_workshop=models.CharField(max_length=30)
    
    
class proshow(models.Model):
    sno=models.IntegerField()
    title=models.CharField(max_length=20)
    time=models.TimeField()
    date=models.DateField()
    
