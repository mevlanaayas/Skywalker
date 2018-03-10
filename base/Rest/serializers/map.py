# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from base.models import Map


class MapSerializer(ModelSerializer):
    """

    """
    labels = SerializerMethodField()
    label_data = serializers.CharField(write_only=True)

    @staticmethod
    def get_labels(obj):
        return obj.labels()

    class Meta:
        """

        """
        model = Map
        fields = ('id', 'name', 'labels', 'movement_data', 'map_data', 'label_data')

    def create(self, validated_data):
        label_data = validated_data['label_data']
        del validated_data['label_data']
        return super(MapSerializer, self).create(validated_data)
