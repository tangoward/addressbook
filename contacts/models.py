from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
# Create your models here.


class RegUser(User):

    def __str__(self):
        return self.user.username


class ContactPerson(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    contact_number = PhoneNumberField()
    contact_owner = models.ForeignKey(User, related_name='contact_persons', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
