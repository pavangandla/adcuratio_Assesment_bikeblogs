from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Bike(models.Model):
    USERNAME=models.ForeignKey(User,on_delete=models.CASCADE)
    BNAME=models.CharField(max_length=100)
    BID=models.IntegerField(primary_key=True)
    BPRICE=models.CharField(max_length=100)
    BMODEL=models.CharField(max_length=100)
    BCAPACITY=models.CharField(max_length=100)
    BWEIGHT=models.CharField(max_length=100)
    BMILEAGE=models.CharField(max_length=100)
    BIMAGE=models.ImageField()
    DESCRIPTION = models.TextField()

    def __str__(self):
        return self.BNAME