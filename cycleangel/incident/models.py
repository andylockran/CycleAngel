from django.db import models
from django.contrib.auth.models import User
from geoposition.fields import GeopositionField
from rest_framework import routers, serializers, viewsets
from django.contrib import admin

# Create your models here.

class Incident(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField()
    location = GeopositionField()
    reporter = models.ForeignKey(User, related_name="reporter",on_delete=models.SET_NULL,null=True)
    assignee = models.ForeignKey(User, related_name="assignee",on_delete=models.SET_NULL,null=True)
    message = models.TextField(max_length=400)
	#request  # to be defined
    def __str__(self):
        return self.title


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ('title', 'time', 'location', 'message','reporter')

# ViewSets define the view behavior.
class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class IncidentAdmin(admin.ModelAdmin):
    list_display = ('title','reporter')
    list_filter = ('time',)

admin.site.register(Incident,IncidentAdmin)