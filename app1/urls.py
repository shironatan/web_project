from django.conf import settings
from django.urls import include
from django.conf.urls import url
from django.contrib.auth import views as auth_view


from . import views

urlpatterns = [
    url(r'^$', views.home_view,name='home'),
    url(r'^auth/', include('allauth.urls')),
    url(r'^signin/?$', views.signin_view,name='account_login'),
    url(r'^signup/?$', views.signup_view,name='account_signup'),
    url(r'^signout/?$',views.signout_view,name='account_signout'),
]