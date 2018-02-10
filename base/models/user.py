# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from base.models.map import Map
from django.shortcuts import get_object_or_404


class CustomUser(AbstractUser):
    contact = models.CharField(max_length=100, unique=True)
    positionID = models.IntegerField(null=True)
    coords = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = 'auth_user'
        app_label = 'base'

    def map(self):
        result = get_object_or_404(Map, id=self.positionID)
        return result
        # returns map that has id of positionID
