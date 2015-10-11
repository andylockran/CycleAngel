from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse,render_to_response
from django.template import RequestContext, loader
from account.models import Item
from django.contrib.auth.models import User
import datetime
# Create your views here.


def index(request):
	if request.user.is_authenticated():
		items = Item.objects.filter(owner=request.user)
		social = request.user.social_auth.filter(
    		provider='strava',
		).first()
		a = social.extra_data['athlete']['profile_medium']
		return render_to_response('account.html', {"items": items,"social": social,"image": image }, context_instance=RequestContext(request))
	else:
		return redirect('/') 

