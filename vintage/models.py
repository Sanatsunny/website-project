from django.db import models

# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    fees=models.IntegerField(default="25000")
    image=models.FileField(upload_to="documents",default="default.jpg")
