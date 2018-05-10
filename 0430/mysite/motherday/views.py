from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
# Create your views here.


def post(request):
	name=''
	content=''
	title=''
	if request.method == 'POST':
		name = request.POST['name']
		content = request.POST['content']
		title = request.POST['title']
		Post.objects.create(name=name, title=title, content=content)
	names = Post.objects.all()
	return render_to_response('motherday/post.html', locals())