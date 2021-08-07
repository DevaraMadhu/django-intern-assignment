from django.db import models

# Create your models here.

Male = '1'
Female = '2'
GENDER_CHOICES = (
    (Male, 'Male'),
    (Female, 'Female')
)

class DoctorList(models.Model):
    name = models.CharField(max_length=32)
    fees = models.IntegerField(default=500)

    def __str__(self):
        return self.name


class PatientList(models.Model):
    first_name =  models.CharField(max_length=32)
    last_name =  models.CharField(max_length=32)
    gender =  models.CharField(choices=GENDER_CHOICES,max_length=32)
    age =  models.IntegerField()
    disease =  models.CharField(max_length=32)
    doctor_con = models.ForeignKey(DoctorList,on_delete=models.CASCADE)
    started_meds = models.DateTimeField(blank= True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

