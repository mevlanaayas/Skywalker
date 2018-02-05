# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer
from base.models import Map


class MapSerializer(ModelSerializer):
    """

    """
    class Meta:
        """

        """
        model = Map
        fields = '__all__'
