from django.shortcuts import render, HttpResponseRedirect 
from incident.forms import IncidentForm
from incident.models import Incident
from geoposition.fields import Geoposition
import datetime
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
    Incidents = Incident.objects.all().order_by('-time')
    return render(request, 'IncidentList.html', {"Incidents": Incidents})

def new(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            form = IncidentForm()
        else:
            form = IncidentForm(request.POST)
            if form.is_valid():
                print(request.POST)
                title = form.cleaned_data['title']      
                message = form.cleaned_data['message']      
                location = Geoposition(form.cleaned_data['location'][0],form.cleaned_data['location'][1])
                reporter = request.user.id
                saveData = form.save(commit=False)
                saveData.time = datetime.datetime.now()
                saveData.reporter = request.user
                saveData.save()
                id = saveData.pk
                return HttpResponseRedirect(reverse('detail', kwargs={"id" :id }))
                
        return render(request,'IncidentForm.html', {"form": form,})
    else:
        return redirect('/')

def detail(request,id):
    inc = Incident.objects.get(pk=id)
    return render(request,'Incident.html',{"incident": inc,})