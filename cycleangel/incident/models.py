from django.db import models
from django.contrib.auth.models import User
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from geoposition.fields import GeopositionField
from rest_framework import routers, serializers, viewsets

# Create your models here.

class IncidentPage(Page):
	time = models.DateTimeField()
	location = GeopositionField()
	reporter = models.ForeignKey(User, related_name="reporter")
	assignee = models.ForeignKey(User, related_name="assignee")
	message = models.TextField(max_length=400)
	#request  # to be defined



IncidentPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('time', classname="full"),
    FieldPanel('location', classname="full"),
    FieldPanel('reporter', classname="full"),
    FieldPanel('assignee', classname="full"),
    FieldPanel('message', classname="full"),
]


class IncidentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IncidentPage
        fields = ('title', 'time', 'location', 'message')

# ViewSets define the view behavior.
class IncidentViewSet(viewsets.ModelViewSet):
    queryset = IncidentPage.objects.all()
    serializer_class = IncidentSerializer