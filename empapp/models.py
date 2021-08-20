from django.db import models

# Create your models here.
class profile(models.Model):
    name= models.CharField(max_length=20)
    Age= models.IntegerField()
    height=models.FloatField()
    number= models.IntegerField(max_length=12)


    def __str__(self):
        return self.name

