# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField

from base.functions.gzip import gzip_op, map_data_op, process
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
        map_data = validated_data['map_data']
        movement_data = validated_data['movement_data']
        adam_gibi_map_data = gzip_op(map_data)
        adam_gibi_movement_data = gzip_op(movement_data)
        new_map_json = process(adam_gibi_map_data, adam_gibi_movement_data)

        # label_data = validated_data['label_data']
        # ready2use_map_data = map_data_op(adam_gibi_map_data)
        del validated_data['label_data']
        return super(MapSerializer, self).create(validated_data)
