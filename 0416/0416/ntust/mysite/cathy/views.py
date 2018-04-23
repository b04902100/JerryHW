from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Info
# Create your views here.
def index(request):
	info = Info.objects.all()
	return render_to_response('cathy/info.html', locals())