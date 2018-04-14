# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import Map
from base.models.mixins import AuditMixin


class KR(AuditMixin):

    map_id = models.IntegerField(null=True)

    class Meta:
        verbose_name = _('KR')
        verbose_name_plural = _('KRs')
        db_table = 'KRs'
        app_label = 'base'
