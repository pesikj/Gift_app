from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    surname = models.CharField(max_length=50, blank=True, null=True)
    wish = models.ForeignKey('Gift', on_delete=models.CASCADE, blank=True, null=True)


# TODO: one-to-many relationship Person x Gift as wish
# TODO:    Dates = models.ForeignKey(ImportantDates) ?!

# TODO: CALENDAR for birthdays & events
# TODO: CALENDAR for namedays
# TODO: email the notificatons (events, gift updates etc.)

class ImportantDates(models.Model):
    birthday = models.DateField()
    aniversary = models.DateField()


class Gift(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    wished_by = models.ForeignKey('Person', on_delete=models.CASCADE, blank=False, null=False)
    link = models.CharField(max_length=100, blank=True, null=True)
    status_choices = (
        ("N", "New"),
        ("C", "Claimed"),
        ("G", "Given"),
    )
    status = models.CharField(max_length=1, default='N', choices=status_choices)


# TODO one-to-one definiton for gift to person
#    def __str__(self):
#       return self.user.username

# TODO see person as name not as "person object (X)"
