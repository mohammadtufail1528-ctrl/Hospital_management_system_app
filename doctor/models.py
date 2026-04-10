from django.db import models

# Create your models here.

class Doctor(models.Model):
    
    name=models.CharField()
    age=models.CharField()
    phone=models.CharField(max_length=12)
    specilization=models.CharField()
        
    def __str__(self):
        return self.name