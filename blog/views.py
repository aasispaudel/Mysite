from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

posts = [
	{
		'author': 'Aasis',
		'title': 'My blog',
		'content': 'This is the blog content!',
		'date': date(2013, 4, 24)
	},

	{
		'author': 'Michelle',
		'title': 'Hey!!!',
		'content': 'Is P == NP?? ',
		'date': date(1015, 7, 23)
	}
]

# Create your views here.

def home(request):
	context = {'posts': posts}

	return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'title'})