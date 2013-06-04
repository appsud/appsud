from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	country = models.CharField(max_length=75)
	phone = models.BigIntegerField()
	website = models.CharField(max_length=75)
	profile_picture = models.FileField(upload_to="site_media/img/pro_pic/")


class ApplicationDetails(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=75)
	version = models.IntegerField()
	category = models.CharField(max_length=75)
	license = models.CharField(max_length=75)
	description = models.CharField(max_length=75)
	android_version = models.ManyToManyField('AndroidVersion')
	banner = models.FileField(upload_to="site_media/img/apk_screenshot/")
	screenshot1 = models.FileField(upload_to="site_media/img/apk_screenshot/")
	screenshot2 = models.FileField(upload_to="site_media/img/apk_screenshot/")
	screenshot3 = models.FileField(upload_to="site_media/img/apk_screenshot/")
	apk = models.FileField(upload_to="site_media/apk/")
	

class AndroidVersion(models.Model):
	android_version = models.CharField(max_length=100)

admin.site.register(AndroidVersion)


