from django.shortcuts import render 

def index(request): 
	return render(request, 'blog/index.html')

def blog(request):
	return render(request, 'blog/blog.html')