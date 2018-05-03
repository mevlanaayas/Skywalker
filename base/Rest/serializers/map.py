# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer
from base.constants import JSON_KEY_ERROR_MESSAGE
from base.functions.gzip import gzip_op, process, compress_op
from base.models import Map
import logging


class MapSerializer(ModelSerializer):
    """

    """
    class Meta:
        """

        """
        model = Map
        fields = ('id', 'name', 'movement_data', 'map_data', 'label_data', 'qr_id')
        lookup_fields = 'qr_id'

    def create(self, validated_data):
        map_data = validated_data.get('map_data', JSON_KEY_ERROR_MESSAGE)
        movement_data = validated_data.get('movement_data', JSON_KEY_ERROR_MESSAGE)
        extracted_map_data = gzip_op(map_data)
        extracted_movement_data = gzip_op(movement_data)
        new_map_json = process(extracted_map_data, extracted_movement_data)
        new_map_data = compress_op(new_map_json)
        """
        convert zipped map data to map points 
        """
        # label_data = validated_data['label_data']
        # save_label(extract_label_point(label_data))
        validated_data['map_data'] = str(new_map_data)
        return super(MapSerializer, self).create(validated_data)
