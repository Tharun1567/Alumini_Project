from django.db import models

# Create your models here.
class Alumi(models.Model):
    person=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    branch=models.CharField(max_length=100)
    passedOut=models.IntegerField()
    achievements=models.TextField(max_length=2000)
    company=models.CharField(max_length=200)
    role=models.CharField(max_length=50)
    exp=models.IntegerField()
    workLocation=models.CharField(max_length=100)
    gitHub=models.URLField(null=True,blank=True)
    linkedIn=models.URLField(null=True,blank=True)
    portfolio=models.URLField(null=True,blank=True)
    image=models.ImageField(upload_to='media')

    def __str__(self):
        return self.person.username
