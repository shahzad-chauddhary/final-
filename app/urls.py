from . import views
from django.urls import path

urlpatterns = [

    path('',views.Index.as_view(),name='index'),
    path('about', views.About.as_view(), name='about'),
    path('portfolio-work', views.Portfolio_work.as_view(), name='portfolio_work'),
    path('work_details', views.Work_details.as_view(), name='work_details'),
    path('services', views.Services.as_view(), name='services'),
    path('elements', views.Elements.as_view(), name='elements'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('blog',views.Blog.as_view(),name='blog'),
    path('single_blog',views.Single_blog.as_view(),name='single_blog'),

]