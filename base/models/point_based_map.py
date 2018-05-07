# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from base.models import Map
from base.models.mixins import AuditMixin


class PointBasedMap(AuditMixin):
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    advanced_points = models.TextField()
    label_data = models.TextField()
    initial_points = models.TextField()
    movement_points = models.TextField()

    class Meta:
        verbose_name = _('Point Based Map')
        verbose_name_plural = _('Point Based Maps')
        db_table = 'point_based_map'
        app_label = 'base'

    def __unicode__(self):
        return self.map.name + ' ' + self.created_by

    def __str__(self):
        return self.map.name + ' ' + self.created_by

    def get_map(self):
        result = self.map.name
        return result

    def get_qr_id(self):
        result = self.map.qr_id
        return result
