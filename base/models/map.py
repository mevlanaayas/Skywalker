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
        db_table = 'maps'
        app_label = 'base'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def labels(self):
        from base.Rest.serializers.label import LabelSerializer
        from base.models.label import Label
        result = Label.objects.filter(map=self)
        serializer = LabelSerializer(data=result, many=True)
        serializer.is_valid()
        return serializer.data
        # returns labels of map

    def qr(self):
        pass
        # returns qr. don't know it is required. will se
