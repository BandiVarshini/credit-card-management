from django.contrib import admin
from django.urls import path
from .views import *



app_name="creditCard"

urlpatterns = [
    path('add/',AddCardView.as_view(),name='add_card'),
    path('update/<int:pk>',UpdateCard.as_view(),name='update_card'),
    path('delete/<int:pk>',DeleteCard.as_view(),name="delete_card"),
    path('show/',CardsListView.as_view(),name='show_user_cards'),

]

