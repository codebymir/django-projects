from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
#class based views
class HomePageView(TemplateView):
	"""docstring for HomePageView"""
	template_name='home.html'

class AboutPageView(TemplateView):
	"""docstring for AboutPageView"""
	template_name='about.html'
		











#function based views examples below
#def homePageView(request):
#	return HttpResponse('hello, there still confused!')


#for about page
#def aboutPageView(request):
	#return HttpResponse('hello, there now on about page, still doesnot make any sense')
