from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from django.views import generic
from django.views.generic import TemplateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from django.views.generic.edit import UpdateView

# Create your views here.


class MyAccountView(TemplateView):
    template_name = 'account/myaccount.html'

class ShowView(TemplateView):
    template_name = 'account/show.html'

class EditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'account/edit.html'
    success_url = 'myaccount'

    def get_object(self):
        return self.request.user
