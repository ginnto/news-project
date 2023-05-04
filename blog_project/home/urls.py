from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('abouts',views.about,name='about'),
    path('',views.contact,name='contact')
]