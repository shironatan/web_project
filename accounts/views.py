from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

#class PasswordChange(LoginRequiredMixin,PasswordChangeView):
#    success_url = 'registration/password_change_done.html'
#    template_name = 'registration/password_change_form.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['form_name'] = "password_change"
#        return context
