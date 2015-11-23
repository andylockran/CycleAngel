from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib import admin

# Create your models here.

from django.contrib.auth.models import User

from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel,
    MultiFieldPanel)
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from geoposition.fields import GeopositionField


class AccountPage(Page):
	biography = RichTextField(blank=True)

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')

class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

FormPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    InlinePanel('form_fields', label="Form fields"),
    FieldPanel('thank_you_text', classname="full"),
    MultiFieldPanel([
        FieldPanel('to_address', classname="full"),
        FieldPanel('from_address', classname="full"),
        FieldPanel('subject', classname="full"),
    ], "Email")
]

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
	description = RichTextField()
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
