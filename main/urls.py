from . import views

from django.views.generic import TemplateView
from django.urls import include,path
app_name = 'main'


urlpatterns = [
    path('',views.Home.as_view(),name='home'),
]
