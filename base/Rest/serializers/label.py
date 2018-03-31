# -*- coding: utf-8 -*-
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from base.models import Label


class LabelSerializer(ModelSerializer):
    """

    """
    map_name = SerializerMethodField()

    @staticmethod
    def get_map_name(obj):
        return obj.get_map()

    class Meta:
        """

        """
        model = Label
        fields = ('id', 'name', 'coords', 'map_name', 'map')
