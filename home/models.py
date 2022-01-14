from django.db import models


class person(models.Model):
	personid = models.AutoField(primary_key=True)
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	age = models.IntegerField()
	email = models.CharField(max_length=255)
	image = models.ImageField(upload_to='media', default='default.jpg')



class personalDetails(models.Model):
	detailid = models.AutoField(primary_key=True)
	personid = models.ForeignKey(person, on_delete=models.CASCADE)
	phone = models.IntegerField(default=0, null=True)


class designation(models.Model):
	designationid = models.AutoField(primary_key=True)
	personid = models.ForeignKey(person, on_delete=models.CASCADE)
	name = models.CharField(max_length=255, default='', null=True)
