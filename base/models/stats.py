# -*- coding: utf-8 -*-
from django.db import models
from base.models import AuditMixin
from django.utils.translation import ugettext_lazy as ul


class Stats(AuditMixin):
    destination_label = models.CharField(ul('Destination Label'), max_length=255)
    path_length = models.IntegerField(ul('Path Length'))
    down_time = models.IntegerField(ul('Down Time'))

    class Meta:
        verbose_name = ul('Stats')
        verbose_name_plural = ul('Stats')
        db_table = 'stats'
        app_label = 'base'
