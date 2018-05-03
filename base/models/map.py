# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from base.models.mixins import AuditMixin


class Map(AuditMixin):
    name = models.CharField(max_length=100, unique=True)
    map_data = models.TextField()
    movement_data = models.TextField()
    label_data = models.TextField()
    initial_data = models.TextField()
    qr_id = models.IntegerField(null=True, unique=True)

    class Meta:
        verbose_name = _('Map')
        verbose_name_plural = _('Maps')
        db_table = 'maps'
        app_label = 'base'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
