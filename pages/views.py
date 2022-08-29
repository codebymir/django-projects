from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePageView(request):
	return HttpResponse('hello, there still confused!')


#for about page
#def aboutPageView(request):
	#return HttpResponse('hello, there now on about page, still doesnot make any sense')
