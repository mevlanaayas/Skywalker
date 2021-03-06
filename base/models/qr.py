# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from base.models.mixins import AuditMixin


class KR(AuditMixin):
    map_id = models.IntegerField(null=True)
    email = models.EmailField()

    class Meta:
        verbose_name = _('KR')
        verbose_name_plural = _('KRs')
        db_table = 'krs'
        app_label = 'base'
