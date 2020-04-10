from django.shortcuts import render
from django.views.generic import ListView
from .models import Page,SubMenu


class Home(ListView):
	template_name = 'app/index.html'
	queryset = Page.objects.all()
	context_object_name = 'page'



class About(ListView):
	template_name = 'app/about.html'
	queryset = Page.objects.all()
	context_object_name = 'page'


class Portfolio_work(ListView):
    template_name = 'app/portfolio-work.html'
    queryset = Page.objects.all()
    context_object_name = 'page'

class Work_details(ListView):
    template_name = 'app/work_details.html'
    queryset = Page.objects.all()
    context_object_name = 'page'

class Services(ListView):
    template_name = 'app/services.html'
    queryset = Page.objects.all()
    context_object_name = 'page'

class Elements(ListView):
    template_name = 'app/elements.html'
    queryset = Page.objects.all()
    context_object_name = 'page'

class Contact(ListView):
    template_name = 'app/contact.html'
    queryset = Page.objects.all()
    context_object_name = 'page'

class Blog(ListView):
    template_name = 'app/blog.html'

class Single_blog(ListView):
    template_name = 'app/single-blog.html'
    queryset = Page.objects.all()
    context_object_name = 'page'


