from django.db import models

# Create your models here.
class Topics(models.Model):
   
    TName=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.TName

class Webpages(models.Model):
    TName=models.ForeignKey(Topics,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100,unique=True)
    Email=models.EmailField(default='sbharath143@gmail.com')
    Url=models.URLField()

    def __str__(self):
        return self.Name

class AccessRecord(models.Model):
    Name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
    Author=models.CharField(max_length=100)
    Date=models.DateField()

    def __str__(self):
        return self.Date