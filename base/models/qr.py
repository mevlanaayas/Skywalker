# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from base.models.mixins import AuditMixin


class KR(AuditMixin):
    """
    User send KR create request.
    User is going to place created KR to the wall/door/etc.
    Constraints:
        User must match wall and mobile phone cameras before sending request
        Request must include following parameters:
            face : which direction that user is looking at start position
            .
            .
            .
            need more detail

    Note: More than one KR on the same map.
    .
    .
    .
    need more detail
    """
    map_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, null=True)
    face = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = _('KR')
        verbose_name_plural = _('KRs')
        db_table = 'KRs'
        app_label = 'base'

    def __unicode__(self):
        return self.map_name + ' ' + self.position

    def __str__(self):
        return self.map_name + ' ' + self.position
