# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

from appsud.my_choices import COUNTRY_CHOICES,categories,versions


class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class':'span4'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email','class':'span4'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':u"●●●●●●●",'class':'span4'}))
	choice_field = forms.ChoiceField(widget=forms.Select(attrs={'class':'span4'}), choices=COUNTRY_CHOICES)
	phone = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Phone Number','class':'span4'}))
	website = forms.URLField(widget=forms.TextInput(attrs={'placeholder':'Enter your website','class':'span4'}))
	propic = forms.ImageField(widget=forms.FileInput)


class UploadForm(forms.Form):
	app_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Application Name','class':'span4','data-bvalidator':"required"}))
	version = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Version','class':'span4','data-bvalidator':"required,digit"}))
	category = forms.ChoiceField(widget=forms.Select(attrs={'class':'span4'}), choices=categories)
	license_fields = (("Freeware","Freeware"),("Demo Version","Demo Version"))
	license = forms.ChoiceField(widget=forms.Select(attrs={'class':'span4'}), choices=license_fields)
	description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Decribe your app here','class':'span4'}))
	android_version = forms.MultipleChoiceField(widget=CheckboxSelectMultiple,choices=versions)
	display_banner = forms.ImageField(widget=forms.FileInput(attrs={'data-bvalidator':"required,image"}))
	screenshot1 = forms.ImageField(widget=forms.FileInput(attrs={'data-bvalidator':"required,image"}))
	screenshot2 =  forms.ImageField(widget=forms.FileInput(attrs={'data-bvalidator':"required,image"}))
	screenshot3 = forms.ImageField(widget=forms.FileInput(attrs={'data-bvalidator':"required,image"}))
	apk = forms.FileField(widget=forms.FileInput(attrs={'id':'apk_upload','data-bvalidator':"extension[apk],required,"}))




