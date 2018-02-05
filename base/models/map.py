# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from base.models.mixins import AuditMixin


class Map(AuditMixin):
    name = models.CharField(max_length=100, unique=True)
    point_set = models.TextField()

    class Meta:
        verbose_name = _('Map')
        verbose_name_plural = _('Maps')
        db_table = 'base_maps'
        app_label = 'base'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def labels(self):
        pass
        # returns labels of map

    def qr(self):
        pass
        # returns qr. don't know it is required. will se
