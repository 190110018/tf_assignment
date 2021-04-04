from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE,null=True)
    phone = models.CharField(max_length=200, null=True)
    adress = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_images',max_length=100,blank=True,null=True)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    STATUS = (
        ('completed','completed'),
        ('pending','pending'),
    )
    task = models.CharField(max_length=200, null=True)
    employee = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee.user.username
