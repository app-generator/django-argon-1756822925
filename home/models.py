# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.TextField(max_length=255, null=True, blank=True)
    date_added = models.DateTimeField(blank=True, null=True, default=timezone.now)
    description = models.CharField(max_length=255, null=True, blank=True)
    short_description = models.CharField(max_length=255, null=True, blank=True)
    sku = models.IntegerField(null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    view_count = models.IntegerField(null=True, blank=True)
    purchase_count = models.IntegerField(null=True, blank=True)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Clients(models.Model):

    #__Clients_FIELDS__
    first_name = models.TextField(max_length=255, null=True, blank=True)
    last_name = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    phone = models.TextField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.TextField(max_length=255, null=True, blank=True)
    country = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    last_contacted = models.DateTimeField(blank=True, null=True, default=timezone.now)
    last_order_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Clients_FIELDS__END

    class Meta:
        verbose_name        = _("Clients")
        verbose_name_plural = _("Clients")


class User(models.Model):

    #__User_FIELDS__
    first_name = models.TextField(max_length=255, null=True, blank=True)
    client_count = models.IntegerField(null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    phone = models.TextField(max_length=255, null=True, blank=True)
    profile_picture = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    last_action = models.ForeignKey(Actions, on_delete=models.CASCADE)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Attendance(models.Model):

    #__Attendance_FIELDS__
    went_online = models.DateTimeField(blank=True, null=True, default=timezone.now)
    went_offline = models.DateTimeField(blank=True, null=True, default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tasks_completed = models.IntegerField(null=True, blank=True)

    #__Attendance_FIELDS__END

    class Meta:
        verbose_name        = _("Attendance")
        verbose_name_plural = _("Attendance")


class Sales(models.Model):

    #__Sales_FIELDS__
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Clients, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    sale_id = models.IntegerField(null=True, blank=True)
    total = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Sales_FIELDS__END

    class Meta:
        verbose_name        = _("Sales")
        verbose_name_plural = _("Sales")


class Actions(models.Model):

    #__Actions_FIELDS__
    action_name = models.TextField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    comment = models.CharField(max_length=255, null=True, blank=True)

    #__Actions_FIELDS__END

    class Meta:
        verbose_name        = _("Actions")
        verbose_name_plural = _("Actions")


class Stats(models.Model):

    #__Stats_FIELDS__
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    attended_hours = models.DateTimeField(blank=True, null=True, default=timezone.now)
    sales_number = models.IntegerField(null=True, blank=True)
    calls_made = models.TextField(max_length=255, null=True, blank=True)
    emails_sent = models.TextField(max_length=255, null=True, blank=True)

    #__Stats_FIELDS__END

    class Meta:
        verbose_name        = _("Stats")
        verbose_name_plural = _("Stats")



#__MODELS__END
