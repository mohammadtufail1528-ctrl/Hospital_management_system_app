from django.db import models

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    gender=[
        ('male','male'),
        ('female','female'),
        ('other','other'),
    ]
    gender=models.CharField(choices=gender)
    
    phone=models.CharField(max_length=15)
    blood_group=[
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('Ab','Ab'),
        ('O+','O+'),
        ('O-','O-'),
        ('Ab-','Ab+'),
    ]
    blood=models.CharField(choices=blood_group)
    address=models.TextField(max_length=200)    
    
    def __str__(self):
        return self.name