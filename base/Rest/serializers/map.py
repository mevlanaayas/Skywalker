# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from base.models import Map


class MapSerializer(ModelSerializer):
    """

    """
    labels = SerializerMethodField()

    def get_labels(self, obj):
        return obj.labels()

    class Meta:
        """

        """
        model = Map
        fields = ('name', 'point_set', 'labels', 'created_at', 'created_by', 'updated_at', 'updated_by')
