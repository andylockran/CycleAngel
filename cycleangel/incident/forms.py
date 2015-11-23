from django.forms import ModelForm  
from incident.models import Incident


class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = ['title','location','message']
