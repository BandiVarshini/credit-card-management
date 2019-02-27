from django.views import View
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django import forms
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth import authenticate, login, logout
from http.client import HTTPResponse
# Create your views here.


class CardsListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Card
    context_object_name = 'dataSet'
    template_name = 'user_cards_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CardsListView, self).get_context_data(**kwargs)
        cards=list(Card.objects.all().filter(user=self.request.user))
        context.update({
            'title': 'Cards List',
            'user_permissions': self.request.user.get_all_permissions(),
            'dataSet':cards,
        })
        return context

class AddCard(forms.ModelForm):
    class Meta:
        model = Card
        exclude = ['id','user']



class AddCardView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Card
    form_class = AddCard
    template_name = "add_card.html"
    success_url = reverse_lazy("creditCard:show_user_cards")

    def post(self, request, *args, **kwargs):
        card_form = AddCard(request.POST)
        if card_form.is_valid():
            card = card_form.save(commit=False)
            card.user = request.user
            card.save()
            return redirect('creditCard:show_user_cards')
        else:
            return redirect('creditCard:add_card')

class UpdateCard(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url = '/login/'

    model = Card
    form_class = AddCard
    template_name = 'add_card.html'
    success_url = reverse_lazy('creditCard:show_user_cards')

    def has_permission(self):
        card_key = self.kwargs['pk']
        card_details = Card.objects.get(id=card_key)
        return card_details.user  == self.request.user

class DeleteCard(DeleteView):
    model = Card
    template_name = "delete_card.html"
    success_url = reverse_lazy('creditCard:show_user_cards')




