# -*- coding: utf-8 -*-
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from base.models import PointBasedMap


class PointBasedMapSerializer(ModelSerializer):
    """

    """
    map_name = SerializerMethodField()
    qr_id = SerializerMethodField()

    @staticmethod
    def get_map_name(obj):
        return obj.get_map()

    @staticmethod
    def get_qr_id(obj):
        return obj.get_qr_id()

    class Meta:
        """

        """
        model = PointBasedMap
        fields = ('id', 'map_name', 'qr_id', 'created_by' 'advanced_points', 'label_data', 'initial_points', 'movement_points')

