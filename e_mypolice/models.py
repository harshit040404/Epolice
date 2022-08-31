from django.db import models

# Create your models here.

class login_data (models.Model):
    fullname=models.CharField(max_length=50)
    email_id=models.EmailField()
    passwrd=models.CharField(max_length=20)
    city=models.CharField(max_length=20)

class contactus(models.Model):
    name=models.CharField(max_length=50)
    phone_number=models.BigIntegerField()
    email_id=models.EmailField()
    msg=models.TextField()

class fir(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    mobile=models.IntegerField()
    city=models.CharField(max_length=20)
    zip=models.IntegerField()
    details=models.TextField()

class missingperson(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    city=models.CharField(max_length=20)
    zip=models.IntegerField()
    details=models.TextField()

class stolenproperty(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    city=models.CharField(max_length=20)
    zip=models.IntegerField()
    details=models.TextField()
    pid=models.CharField(max_length=100)