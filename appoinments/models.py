from django.db import models

# Create your models here.
class Appoinment(models.Model):
    patient = models.ForeignKey('patient.Patient',on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctor.Doctor',on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField(null=True, blank=True)

    
    
   
    def __str__(self):
        return f"Appoinment for {self.patient} with {self.doctor} on {self.date} at {self.time}"