from . import views

from django.views.generic import TemplateView
from django.urls import include,path
app_name = 'main'


urlpatterns = [
    path('',TemplateView.as_view(template_name='home.html'),name='home'),
]
