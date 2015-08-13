from django.db import models
from django.contrib import admin

# Create your models here.

from django.contrib.auth.models import User

from wagtail.wagtailcore.fields import RichTextField


class Account(models.Model):
	user = models.ForeignKey(User)
	public = models.BooleanField()
	last_location = models.CharField(max_length=400,blank=True)


class StaticLocations(models.Model):
	name = models.CharField(max_length=400, blank=True)
	location = models.CharField(max_length=400, blank=True)
	privacy = models.CharField(max_length=40,blank=True)
	items = models.ManyToManyField('Item')


class Item(models.Model):
	name = models.CharField(max_length=400)
	owner = models.ForeignKey(User,related_name="Owner")
	holder = models.ForeignKey(User,related_name="Holder")
	value = models.IntegerField(blank=False)
	manufacturer = models.ForeignKey('Manufacturer')
	variation = models.ForeignKey('Variation')
	description = RichTextField
	transferable = models.BooleanField()

	def __str__(self):
		return self.name


class Manufacturer(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name 

class Variation(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name


class AccountAdmin(admin.ModelAdmin):
	pass

class StaticLocationsAdmin(admin.ModelAdmin):
	pass

class ItemAdmin(admin.ModelAdmin):
	pass

class ManufacturerAdmin(admin.ModelAdmin):
	pass

class VariationAdmin(admin.ModelAdmin):
	pass



admin.site.register(Account,AccountAdmin)
admin.site.register(StaticLocations,StaticLocationsAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Manufacturer,ManufacturerAdmin)
admin.site.register(Variation,VariationAdmin)