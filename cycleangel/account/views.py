from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse,render_to_response
from django.template import RequestContext, loader
from account.models import Item
import datetime
# Create your views here.


def index(request):
	if request.user.is_authenticated():
		items = Item.objects.filter(owner=request.user)
		return render_to_response('account.html', {"items": items }, context_instance=RequestContext(request))
	else:
		return redirect('/') 

