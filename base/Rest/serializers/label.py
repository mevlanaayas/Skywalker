# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer
from base.models import Label


class LabelSerializer(ModelSerializer):
    """

    """
    class Meta:
        """

        """
        model = Label
        fields = '__all__'
