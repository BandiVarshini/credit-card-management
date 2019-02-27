from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django import forms
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth import authenticate, login, logout
import ipdb

class LogInForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput())
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class LoginFormView(View):

    def get(self, request, *args, **kwargs):
        form = LogInForm()
        return render(
            request,
            template_name='login_form.html',
            context={
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:

                login(request,user)
                return redirect('creditCard:show_user_cards')
            else:
                return redirect('login_form')

class LogOut(View):
    def get(self,request):
        logout(request)
        return redirect('login_form')