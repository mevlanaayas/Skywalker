# -*- coding: utf-8 -*-
from django.db import models
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from base.models.map import Map
from base.models.mixins import AuditMixin


class Label(AuditMixin):
    name = models.CharField(max_length=100)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    coords = models.CharField(max_length=100)

    class Meta:
        unique_together = ('name', 'map')
        verbose_name = _('Label')
        verbose_name_plural = _('Labels')
        db_table = 'labels'
        app_label = 'base'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_map(self):
        result = get_object_or_404(Map, id=self.map.id)
        return result
        # returns map that has relation with this label
