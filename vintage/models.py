from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    fees=models.IntegerField(default="25000")
    image=models.FileField(upload_to="documents",default="default.jpg")

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=100)
    phone_number=models.IntegerField(default='1234567890')
    dateofbirth=models.DateField
