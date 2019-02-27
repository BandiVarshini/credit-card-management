from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Card(models.Model):
    name_on_the_card = models.CharField(max_length=30)
    expiry_date = models.DateField()
    type = models.CharField(max_length=20)
    cvv = models.IntegerField()
    card_number = models.CharField(max_length=20)

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name_on_the_card
