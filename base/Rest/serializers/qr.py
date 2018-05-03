# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer
from base.models import KR


class KRSerializer(ModelSerializer):
    """

    """

    class Meta:
        """

        """
        model = KR
        fields = ['id', 'created_by', 'email']
        read_only_fields = ['map_id']

